from contextlib import contextmanager
import os
from typing import Generator

from dotenv import load_dotenv
import psycopg2
from psycopg2.extensions import connection


load_dotenv()

pg_pass = os.getenv("POSTGRES_PASS")
pg_host = os.getenv("POSTGRES_HOST")
pg_port = os.getenv("POSTGRES_PORT")

dsn_str = f"host={pg_host} dbname=postgres user=postgres password={pg_pass} port={pg_port}"


@contextmanager
def create_connection(db_file) -> Generator[connection, None, None]:
    conn = psycopg2.connect(dsn_str)
    yield conn
    conn.rollback()
    conn.close()
