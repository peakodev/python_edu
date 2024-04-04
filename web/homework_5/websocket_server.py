from datetime import datetime

import asyncio
import names
from websockets import (
    serve,
    WebSocketServerProtocol,
    ConnectionClosedOK,
    WebSocketProtocolError
)
from aiofile import async_open

from logger import logger
from exchanger import ExchangeRateFetcher

URL = 'localhost'
PORT = 7070


def parse_exchange_command(input_string: str):
    command, *arguments = input_string.split(' ')
    argument = int(arguments[0]) if arguments else 1
    return command, argument


class ChatServer:
    clients = set()

    async def register(self, ws: WebSocketServerProtocol):
        ws.name = names.get_full_name()
        self.clients.add(ws)
        logger.info(f'{ws.remote_address} connects. Name: {ws.name}')
        await self.send_to_client(ws, f"Joined with name {ws.name}!")
        await self.send_to_clients(ws, "joined the chat.")

    async def unregister(self, ws: WebSocketServerProtocol):
        self.clients.remove(ws)
        logger.info(f'{ws.remote_address} disconnects')
        await self.send_to_clients(ws, "left the chat.")

    async def send_to_clients(self, sender: WebSocketServerProtocol, message: str):
        if self.clients:
            for client in self.clients:
                msg = f"{sender.name}: {message}" if client != sender else f"Me: {message}"
                await self.send_to_client(client, msg)

    async def ws_handler(self, ws: WebSocketServerProtocol):
        await self.register(ws)
        try:
            await self.distrubute(ws)
        except WebSocketProtocolError as err:
            logger.error(err)
        except ConnectionClosedOK:
            pass
        finally:
            await self.unregister(ws)

    async def distrubute(self, ws: WebSocketServerProtocol):
        async for message in ws:
            logger.info(f"Received message from {ws.name}: {message}")
            if not message:
                continue
            if message.startswith('exchange'):
                await self.run_exchange(ws, message)
            else:
                await self.send_to_clients(ws, message)

    async def send_to_client(self, ws: WebSocketServerProtocol, message: str, logger_afp=None):
        await ws.send(message)
        if logger_afp:
            await logger_afp.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {message}\n")

    async def run_exchange(self, ws: WebSocketServerProtocol, message: str):
        async with async_open("exchange.log", 'a+') as afp:
            await self.send_to_client(ws, f"{ws.name}: exchanging ...", afp)
            _, days = parse_exchange_command(message)
            fetcher = ExchangeRateFetcher(days)
            await fetcher.fetch()
            if not fetcher.rates:
                await self.send_to_client(ws, f"{ws.name}: No exchange rates found", afp)
            else:
                [await self.send_to_client(ws, f"{ws.name}: {row}", afp) for row in fetcher.to_strings()]


async def main():
    server = ChatServer()
    async with serve(server.ws_handler, URL, PORT):
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    asyncio.run(main())
