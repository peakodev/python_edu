numbers = [1, 2, 3, 4, 5]

mapped = map(lambda x: x ** 2, numbers)

print(list(mapped))

for i in mapped:
    print(i)