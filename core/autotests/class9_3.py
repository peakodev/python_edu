def complicated(x, y):
    return x / y


def logged_func(func):
    def inner(x, y):
        print(f'called with {x}, {y}')
        result = func(x, y)
        print(f'result: {result}')
        return result
    return inner


complicated = logged_func(complicated)

complicated(10, 2)