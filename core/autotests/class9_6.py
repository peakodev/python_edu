check = range(33)

print(type(check))

def gen():
    yield 12

gen_obj = gen()

print(next(gen_obj))

print(type(gen_obj))