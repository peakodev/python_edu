from functools import reduce

def func(x, y):
    print(x, y, sep=' ')
    return f"{x}{y}"

res = reduce(func, ['a', 'b', 'c', 'e'])

print(res)