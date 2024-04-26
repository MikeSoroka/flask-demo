import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from DB_Classes import *
from data_entries import *

def idListByClass(className, db = 'database.db'): #type:(str, str) -> list
    res = []
    connection = get_db_connection(db)
    currentClass = classAdresses[className]
    for row in currentClass.select(connection):
        res.append(row[currentClass.id])
    return res

def idListByFK(FK, db = 'database.db'): #type:(foreignKey, str) -> list
    res = []
    connection = get_db_connection(db)
    currentClass = FK.Class
    for row in currentClass.select(connection):
        res.append(row[currentClass.id])
    return res

#transforms string of type <smth>s to <SMTH>
def tableNameToClassName(link):
    return link[:-1].upper()

classAdresses = {"users": User,
                "courses": Course,
                "lectures": Lecture,
                "user_lectures": UserLecture,}


def get_db_connection(db = 'database.db'):
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    return connection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'smth'


def attributePossibleValues(currentClass, attribute):
    currentAttribute = getattr(currentClass, attribute)
    return currentAttribute

@app.template_filter('connectedToFK')
def connected(FK):
    return idListByFK(FK)

@app.template_filter('attributeType')
def attributeType(attribute):
    print(type(attribute))
    if isinstance(attribute, limitedVariantsDataEntry):
        print("M")
        return "M"
    if isinstance(attribute, foreignKey):
        print("FK")
        return "FK"
    print("C")
    return "C"

@app.template_filter('str')
def toString(value):
    return str(value)

@app.template_filter('className')
def className(givenClass):
    return givenClass.stringRepresentation

@app.template_filter('muliple_variables')
def isMultipleVariablesEntry(currentClass, currentAttribute):
    return attributePossibleValues(currentClass, currentAttribute) != None

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

@app.route('/<string:table_name>')
def show(table_name):
    connection = get_db_connection()
    my_class = classAdresses[table_name]
    rows = my_class.select(connection)
    return render_template('table.html', rows=rows, table_class=my_class)

@app.route('/create/<string:table_name>', methods=('GET', 'POST'))
#those lines post all required data in user and rendering create.html
def create(table_name):
    my_class = classAdresses[table_name]
    if request.method == 'POST':
        connection = get_db_connection()
        values = []
        for attribute in my_class.attributes:
            values.append(request.form[str(attribute)])
        my_class.push(connection, *values)
        connection.commit()
        connection.close()
        flash('my_class created successfully!', 'success')
        return redirect(f'/{table_name}')
    return render_template('create.html', model=my_class)

@app.route('/edit/<string:table_name>/<int:element_id>', methods=('GET', 'POST'))
#those lines post all required data in user and rendering create.html
def edit(table_name, element_id):
    connection = get_db_connection()
    my_class = classAdresses[table_name]
    record = my_class.get(connection, element_id)
    print(record.keys())
    if request.method == 'POST':
        values = []
        #values[my_class.id] = request.form.get('id')
        for attribute in my_class.attributes:
            values.append(request.form[str(attribute)])
        my_class.update(connection, element_id, *values)
        connection.commit()
        connection.close()
        flash('my_class edited successfully!', 'success')
        return redirect(f'/{table_name}')
    return render_template('edit.html', model=my_class, record=record)

@app.route('/delete/<string:table_name>/<int:element_id>', methods=('GET', 'POST'))
def delete(table_name, element_id):
    connection = get_db_connection()
    my_class = classAdresses[table_name]
    record = my_class.get(connection, element_id)
    my_class.delete(connection, element_id)
    connection.commit()
    connection.close()
    flash(f'{my_class.stringRepresentation} deleted successfully!', 'success')
    return redirect(f'/{table_name}')