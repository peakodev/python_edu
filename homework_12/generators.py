from entities import PhoneBook


class PhoneBookIterator:
    def __init__(self, book: PhoneBook):
        self.__book = book

    def __iter__(self):
        records = list(self.__book.data.values())
        for i in range(0, len(records)):
            yield records[i]


class PaginatedPhoneBookIterator:
    def __init__(self, book: PhoneBook, page_count: int = 2):
        self.__page_count = page_count
        self.__book = book

    @property
    def page_count(self):
        return self.__page_count

    @page_count.setter
    def page_count(self, page_count):
        if page_count <= 2:
            raise ValueError("Page count have to be greater than 1")
        self.__page_count = page_count

    def __iter__(self):
        records = list(self.__book.data.values())
        for i in range(0, len(records), self.__page_count):
            yield records[i:i + self.__page_count]