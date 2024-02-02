def outer_func(variable='', cache=[]):
    _var = variable
    cache.append(variable)
    def inner_func_one(arg):
        cache.append(arg)
        print(f"Function one with variable {_var} {cache}")

    def inner_func_two(arg):
        cache.append(arg)
        print(f"Function two with variable {_var} {cache}")

    def get_arg():
        return cache

    return inner_func_one, inner_func_two, get_arg


f1, f2, get_arg = outer_func('Hello')

f1('Oleh1')
f2('Oleh2')
f1('Igor1')
f2('Igor2')
print(get_arg())


ff1, ff2, fget_arg = outer_func()

ff1('Oleh1f')
ff2('Oleh2f')
ff1('Igor1f')
ff2('Igor2f')
print(fget_arg())

fff1, fff2, ffget_arg = outer_func('Hellooo1', ['Nazar'])

fff1('Oleh1ff')
fff2('Oleh2ff')
fff1('Igor1ff')
fff2('Igor2ff')
print(ffget_arg())