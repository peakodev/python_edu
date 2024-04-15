import sys

from tabulate import tabulate
from termcolor import colored

from connection import create_connection, dsn_str

# Convert sys.argv to an iterator and skip the script name
argv_iter = iter(sys.argv)
next(argv_iter)


class ParamExceptions(Exception):
    pass


class Handler:
    query_parameters = {
        1: None,
        2: ('subject',),
        3: ('subject',),
        4: None,
        5: ('%teacher%',),
        6: ('group',),
        7: ('group', 'subject'),
        8: ('%teacher%',),
        9: ('%student%',),
        10: ('%student%', '%teacher%'),
        11: ('%student%', '%teacher%'),
        12: ('group', 'subject', 'group', 'subject')
    }

    def __init__(self, callback, query_number: str):
        if int(query_number) not in self.query_parameters:
            raise ValueError()
        self.__query_number = query_number
        self.__query = self.__get_query()
        self.__params = self.__ask_params(callback)

    def execute(self):
        with create_connection(dsn_str) as conn:
            with conn.cursor() as cur:
                print('Executing query:\n')
                q_str = cur.mogrify(self.__query, self.__params).decode() + '\n'
                print(colored(q_str, 'cyan'))
                cur.execute(self.__query, self.__params)
                rows = cur.fetchall()
                print(tabulate(rows, headers=[desc[0] for desc in cur.description]))
            print(colored('\nQuery executed successfully\n', 'green'))

    def __ask_params(self, callback):
        str_params = self.query_parameters.get(self.__query_number)
        if not str_params:
            return None
        processed_params = {}
        params = []
        for str_param in str_params:
            if not processed_params.get(str_param):
                processed_params[str_param] = callback(str_param.replace('%', ''))
            val = processed_params[str_param]
            if str_param.startswith('%'):
                val = f'%{val}'
            if str_param.endswith('%'):
                val = f'{val}%'
            params.append(val)
        for param, param_value in processed_params.items():
            if not param_value:
                raise ParamExceptions(f'Please provide {param} value')
        return tuple(params)

    def __get_query(self):
        with open(f'queries/query_{self.__query_number}.sql', 'r') as file:
            return file.read()


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
