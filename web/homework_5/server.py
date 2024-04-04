import asyncio
import names
from websockets import (
    serve,
    WebSocketServerProtocol,
    ConnectionClosedOK,
    WebSocketProtocolError
)

from logger import logger
from exchanger import ExchangeRateFetcher

URL = 'localhost'
PORT = 8080


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
        await self.send_to_clients(f"New chatter: {ws.name}")

    async def unregister(self, ws: WebSocketServerProtocol):
        self.clients.remove(ws)
        logger.info(f'{ws.remote_address} disconnects')
        await self.send_to_clients(f"{ws.name} left the chat.")

    async def send_to_clients(self, message: str):
        if self.clients:
            [await client.send(message) for client in self.clients]

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
                await self.send_to_clients(f"Exchanger (from {ws.name}): exchanging ...")
                _, days = parse_exchange_command(message)
                fetcher = ExchangeRateFetcher(days)
                await fetcher.fetch()
                if not fetcher.rates:
                    await self.send_to_clients(f"Exchanger (from {ws.name}): No exchange rates found")
                    continue
                else:
                    [await self.send_to_clients(f"Exchanger: {row}") for row in fetcher.to_strings()]
            else:
                await self.send_to_clients(f"{ws.name}: {message}")


async def main():
    server = ChatServer()
    async with serve(server.ws_handler, URL, PORT):
        await asyncio.Future()  # run forever

if __name__ == '__main__':
    asyncio.run(main())
