import base64

base64_message = "YWxhZGRpbjpvcGVuc2VzYW1l"

base64_bytes = base64_message.encode('utf-8')
message_bytes = base64.b64decode(base64_bytes)
message = message_bytes.decode('utf-8')
print(message)
