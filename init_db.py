import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
cur.execute("INSERT INTO USERS (name, surname, country, gender) VALUES (?, ?, ?, ?)",
            ('Joseph', 'Stalin', 'USSR', 'Helicopter'))
cur.execute("INSERT INTO USERS (name, surname, country, gender) VALUES (?, ?, ?, ?)",
            ('Theodor', 'Rusevelt', 'USA', 'F-16'))
connection.commit()

connection.close()