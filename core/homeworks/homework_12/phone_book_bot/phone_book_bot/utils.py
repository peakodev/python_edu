import sys
from phone_book import CustomExceptions


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


def show_bot_answer(string):
    sys.stdout.write(string)
    sys.stdout.write('\n')


def input_error(callback_after=None):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except CustomExceptions as inst:
                show_bot_answer(str(inst))
                if callback_after is not None:
                    callback_after()
            except TypeError as te:
                show_bot_answer(str(te))

        return inner
    return decorator
