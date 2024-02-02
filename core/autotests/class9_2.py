

# def outer_func(cache={'counter': 0}):
#
#     def get_arg():
#         cache['counter'] += 1
#         return cache['counter']
#
#     return get_arg()

def outer_func(cache={'counter': 0}):
    cache['counter'] += 1
    return cache['counter']


print(outer_func())
print(outer_func())
print(outer_func())
print(outer_func())
print(outer_func())

def outer_func2(cache=1):
    cache += 1
    return cache



print(outer_func2())
print(outer_func2())
print(outer_func2())
print(outer_func2())
print(outer_func2())
