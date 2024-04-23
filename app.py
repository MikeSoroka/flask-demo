import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from DB_Classes import *

def get_db_connection(db = 'database.db'):
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    return connection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'smth'


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
    connection = get_db_connection()
    users = User.select(connection)
    return render_template('table.html', rows=users, table_class=User)

@app.route('/create', methods=('GET', 'POST'))
#those lines post all required data in user and rendering create.html
def create():
    if request.method == 'POST':
        connection = get_db_connection()
        values = []
        #values[User.id] = request.form.get('id')
        for attribute in User.attributes:
            values.append(request.form[attribute])
        User.push(connection, *values)
        connection.commit()
        connection.close()
        flash('User created successfully!', 'success')
        return redirect(url_for('users'))
    return render_template('create.html', model=User)

@app.route('/edit/<int:user_id>', methods=('GET', 'POST'))
#those lines post all required data in user and rendering create.html
def edit(user_id):
    connection = get_db_connection()
    record = User.get(connection, user_id)
    print(record.keys())
    if request.method == 'POST':
        values = []
        #values[User.id] = request.form.get('id')
        for attribute in User.attributes:
            values.append(request.form[attribute])
        User.update(connection, user_id, *values)
        connection.commit()
        connection.close()
        flash('User edited successfully!', 'success')
        return redirect(url_for('users'))
    return render_template('edit.html', model=User, record=record)

@app.route('/delete/<int:user_id>', methods=('GET', 'POST'))
def delete(user_id):
    connection = get_db_connection()
    record = User.get(connection, user_id)
    User.delete(connection, user_id)
    connection.commit()
    connection.close()
    flash('User deleted successfully!', 'success')
    return redirect(url_for('users'))
