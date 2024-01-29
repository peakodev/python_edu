from entities import AddressBook, Record, AddressBookIterator
from utils import singleton, show_bot_answer, input_error
from exceptions import CommandNotFound


@singleton
class Bot:
    def __init__(self):
        self.__mode = True
        self.__book = None

    @property
    def book(self) -> AddressBook:
        if self.__book is None:
            self.__book = AddressBook.deserialize()
        return self.__book

    @property
    def mode(self) -> bool:
        return self.__mode

    def turn_off(self):
        show_bot_answer("Saving address book into file ... ")
        AddressBook.serialize(self.book)
        self.__mode = False


@input_error()
def add(name, phone, birthday: str = None):
    Bot().book.add_record(Record(name=name, birthday=birthday).add_phone(phone))


@input_error()
def add_phone(name, phone):
    Bot().book.add_phone(name, phone)


@input_error()
def add_birthday(name, birthday):
    Bot().book.add_birthday(name, birthday)


@input_error()
def phone(name):
    phones = Bot().book.get_phones(name)
    show_bot_answer(f'Phones: {', '.join(map(str, phones))}')


def show_all(_):
    for record in AddressBookIterator(Bot().book):
        show_bot_answer(str(record))


def exit_bot(_):
    show_bot_answer('Good Bye!!!')
    Bot().turn_off()


def hello(_):
    show_bot_answer('How can I help you?')
    command_list()


def command_list():
    show_bot_answer(f"Available commands: {', '.join(commands.keys())}")


commands = {
    'add': add,
    'add phone': add_phone,
    'add birthday': add_birthday,
    'get phone': phone,
    'hello': hello,
    'show all': show_all,
    'help': command_list,
    'good bye': exit_bot,
    'close': exit_bot,
    'exit': exit_bot
}


def get_command_handler(command):
    return commands.get(command)


def get_command_from_input(input_string):
    parts = input_string.split()
    for i in range(len(parts), 0, -1):
        command_candidate = ' '.join(parts[:i])
        if command_candidate in commands.keys():
            return command_candidate, input_string[len(command_candidate):]
    raise CommandNotFound


@input_error(callback_after=command_list)
def input_parser(input_string):
    command, input_string = get_command_from_input(input_string)
    parameters = input_string.strip().split(' ')
    command_handler = get_command_handler(command)
    command_handler(*parameters)


def bot_start():
    bot = Bot()
    try:
        while bot.mode:
            input_parser(input("Command: "))
    except KeyboardInterrupt:
        exit_bot(0)
