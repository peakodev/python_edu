from entities import AddressBook, Record, AddressBookIterator, DATE_FORMAT
from utils import singleton, show_bot_answer, input_error
from exceptions import CommandNotFound, CustomExceptions
from faker import Faker
from random import randint
from datetime import date, timedelta


@singleton
class Bot:
    def __init__(self):
        self.__mode = True
        self.__book = None
        self.__commands = {}

    @property
    def book(self) -> AddressBook:
        if self.__book is None:
            self.__book = AddressBook.deserialize()
        return self.__book

    @property
    def mode(self) -> bool:
        return self.__mode

    @property
    def commands(self) -> dict:
        return self.__commands

    @commands.setter
    def commands(self, commands: dict):
        self.__commands = commands

    def turn_off(self):
        show_bot_answer("Saving address book into file ... ")
        AddressBook.serialize(self.book)
        self.__mode = False


@input_error()
def phone(name):
    phones = Bot().book.get_phones(name)
    show_bot_answer(f'Phones: {', '.join(map(str, phones))}')


def generate(count_of_elements):
    if count_of_elements == '':
        count_of_elements = 10
    print(f'\nGenerate random phone book with {count_of_elements} elements ...')
    fake = Faker()
    # Prepare book
    book = AddressBook()
    def_date = date(year=1990, month=1, day=1)
    for i in range(int(count_of_elements)):
        birth = def_date + timedelta(days=i)
        name = fake.first_name_female() if i % 2 else fake.first_name_male()
        if book.find_record(name) is not None:
            name = f'{name} {i}'
        rec = Record(f"{name}", birth.strftime(DATE_FORMAT))
        rec.add_phone(str(randint(1000000000, 9999999999)))
        rec.add_phone(str(randint(1000000000, 9999999999)))
        book.add_record(rec)
        print(rec)

    # Iterate by 3 items per page
    print('\nIterate by 3 items per page:')
    for i, records in enumerate(AddressBookIterator(book, 3)):
        print(f"Portion {i + 1}: ")
        for pi in range(len(records)):
            print(f"{records[pi]}")

    AddressBook.serialize(book)


def show_all(_):
    for record in AddressBookIterator(Bot().book):
        show_bot_answer(str(record))


def exit_bot(_):
    show_bot_answer('Good Bye!!!')
    Bot().turn_off()


def command_list():
    show_bot_answer(f"Available commands: {', '.join(Bot().commands.keys())}")


def get_command_handler(command):
    return Bot().commands.get(command)


@input_error(callback_after=command_list)
def get_command_from_input(input_string):
    parts = input_string.split()
    for i in range(len(parts), 0, -1):
        command_candidate = ' '.join(parts[:i])
        if command_candidate in Bot().commands.keys():
            return command_candidate, input_string[len(command_candidate):]
    raise CommandNotFound


@input_error(callback_after=None)
def command_runner(command, input_string):
    parameters = input_string.strip().split(' ')
    command_handler = get_command_handler(command)
    command_handler(*parameters)


def bot_start():
    bot = Bot()
    bot.commands = {
        'add': bot.book.add,
        'add phone': bot.book.add_phone,
        'add birthday': bot.book.add_birthday,
        'get phone': phone,
        'find': bot.book.find,
        'hello': lambda _: show_bot_answer('How can I help you?'),
        'show all': show_all,
        'help': command_list,
        'generate': generate,
        'good bye': exit_bot,
        'close': exit_bot,
        'exit': exit_bot
    }
    while bot.mode:
        try:
            command_result = get_command_from_input(input("\nCommand: "))
            if command_result is None:
                continue
            command_runner(*command_result)
        except KeyboardInterrupt:
            exit_bot(0)