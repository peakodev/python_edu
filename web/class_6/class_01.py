import sqlite3

with sqlite3.connect('class01.db') as conn:
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Alice', 25))
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Bob', 30))
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Charlie', 35))

    cursor.execute('SELECT * FROM users')
    for row in cursor.fetchall():
        print(row)
