import json
import os
from datetime import datetime

from dotenv import load_dotenv

from db.models import Author, Quote
from db.connect_mongo import connect

load_dotenv()


def get_data() -> tuple:
    with open(os.getenv("QUOTES_PATH"), 'r') as f:
        quotes_data = json.load(f)
    with open(os.getenv("AUTHORS_PATH"), 'r') as f:
        authors_data = json.load(f)
    return quotes_data, authors_data


def seed():
    connect()
    quotes_data, authors_data = get_data()

    for author_data in authors_data:
        new_author = Author(
            fullname=author_data['fullname'],
            born_date=datetime.strptime(author_data['born_date'], '%B %d, %Y'),
            born_location=author_data['born_location'],
            description=author_data['description'])
        new_author.save()

    for quote_data in quotes_data:
        author = Author.objects(fullname=quote_data['author']).first()
        new_quote = Quote(
            quote=quote_data['quote'],
            author=author,
            tags=quote_data['tags'])
        new_quote.save()


if __name__ == '__main__':
    seed()
