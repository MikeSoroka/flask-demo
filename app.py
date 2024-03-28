import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect

def get_db_connection(db = 'database.db'):
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    return connection

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
