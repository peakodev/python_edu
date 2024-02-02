import sys


def logger(func):
    call_number = [0]

    def inner(*args, **kwargs):
        call_number[0] += 1
        sys.stdout.write(f'call: [{call_number[0]}]: [{func.__name__}][{args, kwargs}]\n')
        result = func(*args, **kwargs)
        sys.stdout.write(f'res: [{func.__name__}][{result}]\n')
        return result

    return inner


@logger
def multiplier(a, b, name=''):
    return a * b


multiplier(4, 6, name='Nazar')
multiplier(3, 9)
