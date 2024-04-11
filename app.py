import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from DB_Classes import *

def get_db_connection(db = 'database.db'):
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    return connection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users():
    connection = get_db_connection()
    users = user.select(connection, 1)
    print(users[1].keys())
    return render_template('users.html', users=users)

