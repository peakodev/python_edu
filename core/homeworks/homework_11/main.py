from random import randint
from datetime import date, timedelta
from entities import AddressBook, Record, DATE_FORMAT


def main():
    # Prepare book
    book = AddressBook()
    def_date = date(year=1990, month=1, day=1)
    for i in range(10):
        birth = def_date + timedelta(days=i)
        rec = Record(f"Nazar{i}", birth.strftime(DATE_FORMAT))
        rec.add_phone(str(randint(1000000000, 9999999999)))
        rec.add_phone(str(randint(1000000000, 9999999999)))
        book.add_record(rec)

    # Page
    book.page_count = 3
    # Iterate
    for i, records in enumerate(book):
        print(f"Portion {i + 1}: ")
        for pi in range(len(records)):
            print(f"{records[pi]}")

    for i, records in enumerate(book):
        print(f"Portion {i + 1}: ")
        for pi in range(len(records)):
            print(f"{records[pi]}")


if __name__ == '__main__':
    main()
