# WAS
class Person:
    def __init__(self, name, zip, city, street):
        self.name = name
        self.zip = zip
        self.city = city
        self.street = street

    def get_address(self):
        return f'{self.zip}, {self.city}, {self.street}'


person = Person('Alexander', '36007', 'Poltava', 'European, 28')
print(person.get_address())


# Single responsibility

class PersonAddress:
    def __init__(self, zip, city, street):
        self.zip = zip
        self.city = city
        self.street = street

    def value_of(self):
        return f'{self.zip}, {self.city}, {self.street}'


class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_address(self):
        return self.address.value_of()


if __name__ == '__main__':
    person = Person('Alexander', PersonAddress('36007', 'Poltava', 'European, 28'))
    print(person.get_address())
