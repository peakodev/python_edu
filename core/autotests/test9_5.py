def format_phone_number(func):
    def wrapper(phone):
        phone = func(phone)
        if len(phone) == 10:
            phone = '38' + phone
        if len(phone) == 12:
            phone = '+' + phone
        return phone

    return wrapper


@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone

print(sanitize_phone_number("    +38(050)123-32-34"))
print(sanitize_phone_number("     0503451234"))
print(sanitize_phone_number("(050)8889900"))
print(sanitize_phone_number("38050-111-22-22"))
print(sanitize_phone_number("38050 111 22 11   "))
