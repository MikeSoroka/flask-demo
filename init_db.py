import sqlite3
import os

if os.path.exists('database.db'): os.remove('database.db')
connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

connection.close()