from pymongo import ssl_support
from mongoengine import connect as _connect
from settings import settings as s

URI = f"""mongodb+srv://{s.mongo_user}:{s.mongo_pass}@{s.mongo_domain}/{s.mongo_db_name}?retryWrites=true&w=majority"""


def connect():
    _connect(
        host=URI,
        ssl=True,
        tls=ssl_support.HAVE_SSL,
        tlsAllowInvalidCertificates=True
    )
