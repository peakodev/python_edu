from exceptions import CustomFieldExceptions, WrongNameException, WrongPhoneException, WrongBirthdayException
from collections import UserDict
from datetime import date, datetime
import re


def validator(setter_func):
    def wrapper(self, value):
        try:
            is_valid = self._validate(value)
        except CustomFieldExceptions as e:
            raise e
        # if raise exception is not realized in validate function lets raise it
        if isinstance(is_valid, bool) and not is_valid:
            raise ValueError(f"{self.__class__.__name__}: Invalid value: {value}")

        return setter_func(self, value)

    return wrapper


DATE_FORMAT = '%Y-%m-%d'


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    def _validate(self, value):
        return True

    @property
    def value(self):
        return self._value

    @value.setter
    @validator
    def value(self, value):
        self._value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def _validate(self, value):
        if not (isinstance(value, str) and len(value) > 3):
            raise WrongNameException


class Phone(Field):
    def _validate(self, value):
        pattern = r'\b\d{10}\b'
        if not bool(re.search(pattern, value)):
            raise WrongPhoneException


class Birthday(Field):

    @staticmethod
    def __convert_to_date(date_str: str):
        return datetime.strptime(date_str, DATE_FORMAT).date()

    @Field.value.setter
    @validator
    def value(self, value):
        self._value = self.__convert_to_date(value)

    def _validate(self, value: str):
        try:
            birthday = self.__convert_to_date(value)
        except ValueError:
            raise WrongBirthdayException

        if birthday > date.today():
            raise WrongBirthdayException("Birthday have to be in the past")

    def days_to_birthday(self) -> int:
        today = date.today()
        this_year_birth = date(today.year, self.value.month, self.value.day)
        if this_year_birth < today:
            next_year_birth = date(today.year + 1, self.value.month, self.value.day)
            days_until_birth = (next_year_birth - today).days
        else:
            days_until_birth = (this_year_birth - today).days

        return days_until_birth

    def __str__(self):
        return self._value.strftime(DATE_FORMAT)


class Record:
    birthday = None

    def __init__(self, name, birthday: str = None):
        self.name = Name(name)
        if birthday is not None:
            self.birthday = Birthday(birthday)
        self.phones = []

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)
        return self

    def remove_phone(self, phone):
        phone_obj = self.find_phone(phone)
        if phone_obj:
            self.phones.remove(phone_obj)
        else:
            raise ValueError('Phone not found')

    def edit_phone(self, phone, new_phone):
        self.remove_phone(phone)
        self.add_phone(new_phone)

    def find_phone(self, phone):
        found_phone = list(filter(lambda ph: ph.value == phone, self.phones))
        return found_phone[0] if len(found_phone) else None

    def days_to_birthday(self):
        if self.birthday is not None:
            return self.birthday.days_to_birthday()

    def __str__(self):
        ret = f"Contact name: {self.name.value},"
        if self.birthday is not None:
            ret += f" birthday: {str(self.birthday)}, days to birth: {self.days_to_birthday()},"
        return f"{ret} phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def __init__(self):
        self.__page_count = 0
        super().__init__()

    @property
    def page_count(self):
        return self.__page_count

    @page_count.setter
    def page_count(self, page_count):
        if page_count <= 0:
            raise ValueError("Page count have to be greater than 0")
        self.__page_count = page_count

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        self.data.pop(name, None)

    # This will return iterator
    # def __iter__(self):
    #     self.__counter = 0
    #     self.__countable_data = list(self.data.values())
    #     return self
    #
    # def __next__(self):
    #     if self.__counter >= len(self.__countable_data):
    #         raise StopIteration
    #     self.__counter += self.__page_count
    #     return self.__countable_data[self.__counter - self.__page_count:self.__counter]

    def __iter__(self):
        records = list(self.data.values())
        for i in range(0, len(records), self.__page_count):
            yield records[i:i + self.__page_count]

