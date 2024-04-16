import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from dotenv import load_dotenv


class Base(DeclarativeBase):
    pass


load_dotenv()
DB_URL = os.getenv("POSTGRES_URL")
engine = create_engine(DB_URL)
DBSession = sessionmaker(bind=engine)
session = DBSession()
