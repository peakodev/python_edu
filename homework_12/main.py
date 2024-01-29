from random import randint
from datetime import date, timedelta
from entities import AddressBook, Record, DATE_FORMAT, AddressBookIterator
from bot import bot_start
from faker import Faker


def generate():
    print('\nGenerate random phone book ...')
    fake = Faker()
    # Prepare book
    book = AddressBook()
    def_date = date(year=1990, month=1, day=1)
    for i in range(10):
        birth = def_date + timedelta(days=i)
        name = fake.first_name_female() if i % 2 else fake.first_name_male()
        rec = Record(f"{name}", birth.strftime(DATE_FORMAT))
        rec.add_phone(str(randint(1000000000, 9999999999)))
        rec.add_phone(str(randint(1000000000, 9999999999)))
        book.add_record(rec)

    # Iterate by 3 items per page
    print('\nIterate by 3 items per page:')
    for i, records in enumerate(AddressBookIterator(book, 3)):
        print(f"Portion {i + 1}: ")
        for pi in range(len(records)):
            print(f"{records[pi]}")

    AddressBook.serialize(book)


def show_list():
    print('\nShow all list:')
    book2 = AddressBook.deserialize()
    # Iterate
    for record in AddressBookIterator(book2):
        print(f"{record}")


if __name__ == '__main__':
    generate()
    show_list()
    bot_start()
