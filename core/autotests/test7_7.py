def data_preparation(list_data):
    return_data = []
    if not list_data:
        return return_data
    for slist in list_data:
        if len(slist) > 2:
            return_data.extend(sorted(slist)[1:-1])
        else:
            return_data.extend(slist)
    return sorted(return_data, reverse=True)


def data_preparation_small(list_data):
    flattened = [item for sublist in list_data for item in (sorted(sublist)[1:-1] if len(sublist) > 2 else sublist)]
    return sorted(flattened, reverse=True)


print(data_preparation([[1, 2, 3], [3, 4], [5, 6]]))
print(data_preparation_small([[1, 2, 3], [3, 4], [5, 6]]))
