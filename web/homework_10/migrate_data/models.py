from mongoengine import Document, ReferenceField
from mongoengine.fields import DateTimeField, ListField, StringField


class Author(Document):
    fullname = StringField()
    born_date = DateTimeField()
    born_location = StringField()
    description = StringField()


class Quote(Document):
    quote = StringField()
    author = ReferenceField(Author)
    tags = ListField(StringField())
