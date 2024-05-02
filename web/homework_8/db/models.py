from mongoengine import Document, ReferenceField
from mongoengine.fields import DateTimeField, ListField, StringField, BooleanField


class Author(Document):
    fullname = StringField()
    born_date = DateTimeField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    quote = StringField()
    author = ReferenceField(Author)
    tags = ListField(StringField())


class Contact(Document):
    fullname = StringField()
    email = StringField()
    phone = StringField()
    send_to_phone = BooleanField(default=False)
    is_sent = BooleanField(default=False)
