def all_sub_lists(data):
    sublists = [[]]
    for length in range(1, len(data) + 1):
        for start in range(len(data) - length + 1):
            sublists.append(data[start:start + length])
    return sublists


# print(all_sub_lists([1, 2, 3]))
print(all_sub_lists([4, 6, 1, 3]))
