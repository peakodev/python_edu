import base64


def encode_data_to_base64(data):
    return [base64.b64encode(d.encode('utf-8')).decode('utf-8') for d in data]