def sum_func(x, y):
    return x + y


def subtraction_func(x, y):
    return x - y


def get_operator(operator):
    if operator == '+':
        return sum_func
    elif operator == '-':
        return subtraction_func
    else:
        print('Unknown operator')


print(get_operator("+")(2, 3))  # 5

print(get_operator("-")(2, 3))  # -1

a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))
