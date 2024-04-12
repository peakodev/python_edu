import json
from json import JSONDecodeError
import datetime
import threading


class FileHandler:
    lock = threading.Lock()

    @staticmethod
    def read_file(file_path):
        with open(file_path, 'rb') as f:
            return f.read()

    @staticmethod
    def read_json(file_path):
        with FileHandler.lock:
            with open(file_path, 'r') as f:
                return json.load(f)

    @staticmethod
    def append_json(file_path, data):
        try:
            existing_data = FileHandler.read_json(file_path)
        except FileNotFoundError:
            existing_data = {}
        except JSONDecodeError:
            existing_data = {}

        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")
        existing_data[formatted_time] = data

        with FileHandler.lock:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(existing_data, f)