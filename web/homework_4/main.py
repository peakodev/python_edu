from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, unquote_plus
import mimetypes
from pathlib import Path
import threading
import socket
from dotenv import load_dotenv
import os

from logger import logger
from file_handler import FileHandler

PUBLIC_PATH = Path("front-init")

load_dotenv()
WEB_SERVER_ADDRESS = os.getenv('WEB_SERVER_ADDRESS')
WEB_SERVER_PORT = int(os.getenv('WEB_SERVER_PORT'))
WEB_SOCKET_PORT = int(os.getenv('WEB_SOCKET_PORT'))

STORAGE_DIR = Path(os.getenv('STORAGE_DIR'))
DATA_FILE = os.getenv('DATA_FILE')
DATA_PATH = STORAGE_DIR / Path(DATA_FILE)


class SocketClient:
    def __init__(self, host, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

    def send(self, data):
        self.client_socket.send(data)

    def close(self):
        self.client_socket.close()


class ThreadedSocketServer:
    def __init__(self, host, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))

    def listen(self):
        self.server.listen(5)
        while True:
            client, address = self.server.accept()
            threading.Thread(target=self.handle_client, args=(client, address)).start()

    def handle_client(self, client, address):
        while True:
            data = client.recv(1024)
            if not data:
                break
            data = data.decode()
            logger.debug(f"Received {data} from {address}")
            data = unquote_plus(data)
            dict_data = {key: value for key, value in [el.split("=") for el in data.split("&")]}
            FileHandler().append_json(DATA_PATH, dict_data)
            client.send('OK'.encode())
        client.close()


class BaseHandler(BaseHTTPRequestHandler):
    file_handler = FileHandler()

    def send_static(self, static_filename):
        self.send_response(200)
        mt = mimetypes.guess_type(self.path)
        if mt:
            self.send_header('Content-type', mt[0])
        else:
            self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(self.file_handler.read_file(static_filename))

    def send_html(self, html_filename, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(self.file_handler.read_file(html_filename))


class HttpHandler(BaseHandler):

    PATHES = {
        '/': PUBLIC_PATH / Path("index.html"),
        '/message': PUBLIC_PATH / Path("message.html")
    }

    def do_GET(self):
        url = urlparse(self.path)
        path = self.PATHES.get(url.path)
        if path:
            self.send_html(path)
        else:
            file_path = PUBLIC_PATH / Path(url.path[1:])
            if file_path.exists():
                self.send_static(str(file_path))
            else:
                self.send_html(PUBLIC_PATH / Path("error.html"), 404)

    def do_POST(self):
        data = self.rfile.read(int(self.headers.get('Content-Length')))
        logger.debug(f"{unquote_plus(data.decode())=}")
        resp = self.server.client.send(data)
        logger.debug(f"{resp=}")
        self.send_response(302)
        self.send_header('Location', '/')
        self.end_headers()


def run_http_server(client, server_class=HTTPServer, handler_class=HttpHandler):
    server_address = (WEB_SERVER_ADDRESS, WEB_SERVER_PORT)
    http = server_class(server_address, handler_class)
    http.client = client
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


def run_socket_server():
    socket_server = ThreadedSocketServer(WEB_SERVER_ADDRESS, WEB_SOCKET_PORT)
    socket_server.listen()


def main():
    threading.Thread(target=run_socket_server).start()

    client = SocketClient(WEB_SERVER_ADDRESS, WEB_SOCKET_PORT)
    threading.Thread(target=run_http_server, args=(client,)).start()


if __name__ == '__main__':
    main()
