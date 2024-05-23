import sys
import os
import django

basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(basedir, 'myquotes'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myquotes.settings')
django.setup()

from quotes.models import Author as SqlAuthor, Quote as SqlQuote
from migrate_data.models import Author as MongoAuthor, Quote as MongoQuote
from migrate_data.connect_mongo import connect


def process_data():
    connect()
    for mongo_author in MongoAuthor.objects:
        print(mongo_author.fullname)
        sql_author = SqlAuthor(fullname=mongo_author.fullname, born_date=mongo_author.born_date,
                               born_location=mongo_author.born_location, description=mongo_author.description)
        sql_author.save()
        for mongo_quote in MongoQuote.objects(author=mongo_author.id):
            sql_quote = SqlQuote(quote=mongo_quote.quote, author=sql_author, tags=mongo_quote.tags)
            sql_quote.save()


if __name__ == '__main__':
    process_data()
