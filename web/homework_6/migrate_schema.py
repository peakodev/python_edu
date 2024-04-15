from connection import create_connection, dsn_str


def migrate():
    with create_connection(dsn_str) as conn:
        with conn.cursor() as cur:
            with open('schema.sql', 'r') as f:
                cur.execute(f.read())
        conn.commit()
