import json
from datetime import datetime

from models import Author, Quote
from db.connect_mongo import connect

connect()

with open('quotes.json', 'r') as f:
    quotes_data = json.load(f)

with open('authors.json', 'r') as f:
    authors_data = json.load(f)

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
