limit = 10


def odd_squares(limit):
    for value in range(limit):
        if value % 2:
            yield pow(value, 2)


# get_value = filter(lambda value: bool(value % 2), map(lambda x: pow(x, 2), range(limit)))
get_value = map(lambda x: pow(x, 2), filter(lambda value: bool(value % 2), range(limit)))

for result in zip(get_value, odd_squares(limit)):
    print(result[0], result[1], sep='\t')
