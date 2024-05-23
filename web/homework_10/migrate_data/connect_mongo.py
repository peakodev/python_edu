from pymongo import ssl_support
from mongoengine import connect as _connect
from .conf import config


mongo_user = config.get('Mongo', 'user')
mongodb_pass = config.get('Mongo', 'pass')
db_name = config.get('Mongo', 'db_name')
domain = config.get('Mongo', 'domain')

URI = f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority"""


def connect():
    _connect(host=URI, ssl=True, tls=ssl_support.HAVE_SSL, tlsAllowInvalidCertificates=True)
