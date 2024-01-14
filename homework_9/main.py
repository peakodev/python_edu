import sys

phonebook = {}

STATE = {
    'bot_mode': True
}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyError as inst:
            if func.__name__ == 'phone':
                show_bot_answer('Enter user name')
            else:
                show_bot_answer(str(inst))
        except ValueError as inst:
            if func.__name__ in ['add', 'change']:
                show_bot_answer('Give me name and phone please')
            else:
                show_bot_answer(f'{type(inst)}: {str(inst.args)}')
        except IndexError as inst:
            if func.__name__ in ['add', 'change']:
                show_bot_answer('Enter user name')
            else:
                show_bot_answer(str(inst))

    return inner


def turn_off():
    STATE['bot_mode'] = False


def get_bot_mode():
    return STATE.get('bot_mode')


def show_bot_answer(string):
    sys.stdout.write(string)
    sys.stdout.write('\n')


@input_error
def add(*params):
    name, phone = params
    phonebook[name] = [phone]


@input_error
def change(*params):
    name, phone = params
    phonebook[name].append(phone)


@input_error
def phone(name):
    phones = phonebook[name]
    show_bot_answer(f'Phones: {', '.join(map(str, phones))}')


def show_all(_):
    for name, phones in phonebook.items():
        show_bot_answer(f'Name: {name}, phones: {', '.join(map(str, phones))}')


def exit_bot(_):
    show_bot_answer('Good Bye!!!')
    turn_off()


def hello(_):
    show_bot_answer('How can I help you?')


commands = {
    'add': add,
    'change': change,
    'phone': phone,
    'hello': hello,
    'show all': show_all,
    'good bye': exit_bot,
    'close': exit_bot,
    'exit': exit_bot
}


def get_command_handler(command):
    return commands.get(command)


def get_command_from_input(input_string):
    for prefix in commands.keys():
        if input_string.startswith(prefix):
            return prefix, input_string[len(prefix):]
    raise KeyError('Please provide a valid command')


@input_error
def input_parser(input_string):
    command, input_string = get_command_from_input(input_string)
    parameters = input_string.strip().split(' ')
    command_handler = get_command_handler(command)
    command_handler(*parameters)


def main():
    while get_bot_mode():
        input_parser(input("Command: "))


if __name__ == '__main__':
    main()
