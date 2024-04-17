import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from DB_Classes import *

def get_db_connection(db = 'database.db'):
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    return connection

app = Flask(__name__)


@app.template_filter('table_name')
def getTableName(myClass):
    return myClass.table_name

@app.template_filter('get_attributes')
def getAttributes(myClass):
    return myClass.attributes

@app.template_filter('get_id')
def getID(myClass):
    return myClass.id

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users():
    print(User.attributes)
    connection = get_db_connection()
    users = User.select(connection)
    return render_template('table.html', rows=users, table_class=User)

