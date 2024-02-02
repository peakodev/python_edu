from phone_book import CustomExceptions

class CommandNotFound(CustomExceptions):
    def __init__(self, msg="Command not found. Please provide a valid command."):
        super().__init__(msg)