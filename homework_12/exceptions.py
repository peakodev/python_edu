class CustomFieldExceptions(Exception):
    pass


class WrongNameException(CustomFieldExceptions):
    def __init__(self, msg="Please provide name with at least 3 characters"):
        super().__init__(msg)


class WrongPhoneException(CustomFieldExceptions):
    def __init__(self, msg="Wrong phone number"):
        super().__init__(msg)


class WrongBirthdayException(CustomFieldExceptions):
    def __init__(self, msg="Wrong birthday value: please enter in valid format like '1990-12-20'"):
        super().__init__(msg)



