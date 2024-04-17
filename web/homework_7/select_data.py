import sys

from termcolor import colored

from app.repository import get_select
from app.db import session


# Convert sys.argv to an iterator and skip the script name
argv_iter = iter(sys.argv)
next(argv_iter)


class ParamExceptions(Exception):
    pass


class Handler:
    def __init__(self, callback, query_number: str):
        self.__sql_method, self.__required_params = get_select(int(query_number))
        if self.__sql_method is None:
            raise ValueError()
        self.__params = self.__ask_params(callback)

    def execute(self):
        print('\nExecuting query:\n')
        smt = self.__sql_method(*self.__params)
        print(colored(smt, 'cyan'))
        result = session.execute(smt).fetchall()
        print('\nResult:\n')
        print(result)
        print(colored('\nQuery executed successfully\n', 'green'))

    def __ask_params(self, callback):
        if not self.__required_params:
            return (None,)
        params = []
        for str_param in self.__required_params:
            val = callback(str_param)
            if not val:
                raise ParamExceptions(f'Please provide {str_param} value')
            params.append(val)
        return tuple(params)


def user_communicate(query_number, callback):
    try:
        query_number = int(query_number)
        Handler(callback, query_number).execute()
    except ValueError:
        print('Invalid query number')
    except ParamExceptions as e:
        print(e)


def main():
    query_number = next(argv_iter, None)
    if query_number:
        user_communicate(query_number, lambda _: next(argv_iter, None))
    else:
        while True:
            query_number = input("Enter a query number (1-12) or 'exit' to quit: ")
            if query_number.lower() == 'exit':
                break
            user_communicate(query_number, lambda p: input(f"Enter the {p} name: "))


if __name__ == "__main__":
    main()
