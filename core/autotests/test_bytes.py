
_str = "Nazar Salo"
byte_str = _str.encode()
print(byte_str)
str = str(byte_str, encoding="utf-8")
print(str)
str2 = byte_str.decode()
print(str2)
# decoded = str.decode("utf-8")