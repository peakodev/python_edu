from db.models import Author, Quote
from db.connect_mongo import connect
from db.connect_redis import cache

connect()


@cache
def search_by_author(name):
    author = Author.objects(fullname__icontains=name).first()
    if author:
        quotes = Quote.objects(author=author)
        for quote in quotes:
            return quote.quote
    else:
        return "No quotes found for this author."


@cache
def search_by_tag(tag):
    quotes = Quote.objects(tags__icontains=tag)
    for quote in quotes:
        return quote.quote


def search_by_tags(tags):
    quotes = Quote.objects(tags__in=tags)
    for quote in quotes:
        return quote.quote


while True:
    command = input("Enter command: ")
    if command == "exit":
        break
    else:
        command, value = command.split(":")
        value = value.strip()
        if command == "name":
            print(search_by_author(value))
        elif command == "tag":
            print(search_by_tag(value))
        elif command == "tags":
            tags = value.split(",")
            print(search_by_tags(tags))
