def decode(data):
    if not data:
        return []
    return list(data[0] * data[1]) + decode(data[2:])


d = decode(["Z", 1, "X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2])
print(d)


def encode(data):
    if not data:
        return []
    i = 0
    while i < len(data) and data[0] == data[i]:
        i += 1
    return [data[0], i] + encode(data[i:])


print(encode(d))