def make_request(keys, values):
    ret_dict = {}
    if len(keys) != len(values):
        return ret_dict
    for i in range(len(keys)):
        ret_dict[keys[i]] = values[i]
    return ret_dict


def make_request_simple(keys, values):
    if len(keys) != len(values):
        return {}

    return dict(zip(keys, values))


print(make_request(['key1', 'key2'], ['value1', 'value2']))
print(make_request_simple(['key1', 'key2'], ['value1', 'value2']))
