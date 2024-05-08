import json
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from DB_Classes import *
from data_entries import *

usersTitle = ["ID", "Name", "Surname", "Country", "Gender"]
lecturesTitle = ["ID", "Title", "Course"]
coursesTitle = ["ID", "Name", "Approximate duration", "Overview", "Price"]
userLecturesTitle = ["ID", "Is Completed", "Is Starred", "Lecture", "User"]
gendersTitle = ["ID", "Gender"]

classAdresses = {"users": User,
                "courses": Course,
                "lectures": Lecture,
                "user_lectures": UserLecture,
                "genders": Gender}

def tableFkToDict(table_name, rows):
    if (table_name == "user_lectures"):
        print("UL")
        lect_dict = fkToDict(foreignKey("fk_LECTUREid", Lecture), rows, "title")
        name_dict = fkToDict(foreignKey("fk_USERid", User), rows, "name")

        surname_dict = fkToDict(foreignKey("fk_USERid", User), rows, "surname")

        user_dict = {}
        user_dict.update({foreignKey("fk_USERid", User): {}})
        for ID in list(name_dict.values())[0].keys():
            user_dict[foreignKey("fk_USERid", User)].update({ID: list(name_dict.values())[0][ID] + " " +
                                                                 list(surname_dict.values())[0][ID]})
        return lect_dict | user_dict
    elif (table_name == "users"):
        print("U")
        genders_dict = fkToDict(foreignKey("fk_GENDERid", Gender), rows, "gender")
        return genders_dict

    elif (table_name == "courses"):
        print("C")
        return {}

    elif (table_name == "lectures"):
        courses_dict = fkToDict(foreignKey("fk_COURSEid", Course), rows, "name")
        print("L")
        return courses_dict

def meaningfulClassValues(table_class, db = "database.db"):
    connection = get_db_connection()
    rows = table_class.select(connection)
    if (table_class.table_name == "users"):
        return {str(row["id"]): (row["name"] + " " + row["surname"]) for row in rows}

    elif (table_class.table_name == "courses"):
        return {str(row["id"]):row["name"] for row in rows}

    elif (table_class.table_name == "lectures"):
        return {str(row["id"]):row["title"] for row in rows}

    elif (table_class.table_name == "genders"):
        return {str(row["id"]):row["gender"] for row in rows}

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

def fkToDict(FK, rows, corresponding_attribute, db = 'database.db'):
    res = {}
    res.update({FK: {}})
    connection = get_db_connection(db)
    for row in rows:
        ID = row[str(FK)]
        try:
            (res[FK].update
             ({ID: FK.Class.get(connection, ID)[corresponding_attribute]}))
        except KeyError:
            print("No such attribute")
    return res

#transforms string of type <smth>s to <SMTH>
def tableNameToClassName(link):
    return link[:-1].upper()


def get_db_connection(db = 'database.db'):
    connection = sqlite3.connect(db)
    connection.row_factory = sqlite3.Row
    return connection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'smth'


def attributePossibleValues(currentClass, attribute):
    currentAttribute = getattr(currentClass, attribute)
    return currentAttribute

def connected_classes(Class):
    res = []
    for arg in Class.attributes:
        if isinstance(arg, foreignKey):
            res.append(arg.Class)
    return res


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

@app.template_filter('get_title')
def getTitle(myClass):
    if myClass == User:
        return usersTitle
    elif myClass == Course:
        return coursesTitle
    elif myClass == Lecture:
        return lecturesTitle
    elif myClass == UserLecture:
        return userLecturesTitle

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
    special_attributes = {}
    #foreignKey("fk_USERid", User))
    print(my_class.table_name)
    return render_template('table.html', rows=rows, table_class=my_class,
                           special_attributes=tableFkToDict(my_class.table_name, rows))


@app.route('/create/<string:table_name>', methods=('GET', 'POST'))
#those lines post all required data in user and rendering create.html
def create(table_name):
    my_class = classAdresses[table_name]
    requestedClasses = connected_classes(my_class)
    fkVarsDict = {}
    for Class in requestedClasses:
        fkVarsDict.update({Class: meaningfulClassValues(Class)})

    if request.method == 'POST':
        connection = get_db_connection()
        values = []
        for attribute in my_class.attributes:
            values.append(request.form[str(attribute)])
        my_class.push(connection, *values)
        connection.commit()
        connection.close()
        flash(f'{my_class.stringRepresentation} created successfully!', 'success')
        return redirect(f'/{table_name}')
    return render_template('create.html', model=my_class, fkVars=fkVarsDict)

@app.route('/edit/<string:table_name>/<int:element_id>', methods=('GET', 'POST'))
#those lines post all required data in user and rendering create.html
def edit(table_name, element_id):
    connection = get_db_connection()
    my_class = classAdresses[table_name]
    requestedClasses = connected_classes(my_class)
    record = my_class.get(connection, element_id)
    print(record.keys())
    fkVarsDict = {}
    for Class in requestedClasses:
         fkVarsDict.update({Class: meaningfulClassValues(Class)})
    if request.method == 'POST':
        values = []
        #values[my_class.id] = request.form.get('id')
        for attribute in my_class.attributes:
            values.append(request.form[str(attribute)])
        my_class.update(connection, element_id, *values)
        connection.commit()
        connection.close()
        flash(f'{my_class.stringRepresentation} edited successfully!', 'success')
        return redirect(f'/{table_name}')
    return render_template('edit.html', model=my_class, record=record, fkVars=fkVarsDict)


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

@app.route('/add-fields', methods=['GET', 'POST'])
def add_fields():
    number_of_fields = request.form.get('number_of_fields')
    if not number_of_fields:
        number_of_fields = 1
    elif request.form.get('add'):  # incrementing number of fields if "Add more" button was clicked
        number_of_fields = int(number_of_fields) + 1
    else:  # processing form data
        data = ",".join([f"field_{i}:{request.form.get(f'field_{i}')} " for i in range(int(number_of_fields))])
        print(data)  # replace this with data processing logic
    return render_template('add_multiple_files.html', number_of_fields=number_of_fields)

@app.route('/create/users/<int:entriesAmount>', methods=('GET', 'POST'))
#those lines post all required data in user and rendering create.html
def createMult(entriesAmount):
    table_name="users"
    my_class = classAdresses[table_name]
    requestedClasses = connected_classes(my_class)
    fkVarsDict = {}
    for Class in requestedClasses:
        fkVarsDict.update({Class: meaningfulClassValues(Class)})

    requestedClassesMultiple = connected_classes(Lecture)
    fkVarsDictMultiple = {}
    for Class in requestedClassesMultiple:
        fkVarsDictMultiple.update({Class: meaningfulClassValues(Class)})
    f = open("dict_data", "w")
    f.write(str(fkVarsDictMultiple))
    f.close()

    if request.method == 'POST':
        connection = get_db_connection()
        values = []
        for attribute in my_class.attributes:
            values.append(request.form[str(attribute)])
        my_class.push(connection, *values)
        if my_class.table_name == "users":
            requests = []
            requests_counter = entriesAmount
            for i in range(requests_counter):
                current_requests = []
                for attribute in Lecture.attributes:
                    current_requests.append(request.form[str(attribute) + str(i)])
                requests.append(current_requests)

            intermRequests = []
            for i in range(requests_counter):
                current_requests = []
                for attribute in UserLecture.attributes:
                    if not isinstance(attribute, foreignKey):
                        current_requests.append(request.form[str(attribute) + str(i) + "int"])
                intermRequests.append(current_requests)
            for i in range(len(requests)):
                req = requests[i]
                Lecture.push(connection, *req)
                reqInt = intermRequests[i]
                UserLecture.push(connection, *reqInt, Lecture.last(connection), User.last(connection))

        connection.commit()
        connection.close()
        flash(f'{my_class.stringRepresentation} created successfully!', 'success')
        return redirect(f'/{table_name}')
    if my_class.table_name == "users":
        return render_template('add_multiple_files.html', model=my_class, fkVars=fkVarsDict,
                               multipleAddClass=Lecture, fkAddVars=fkVarsDictMultiple,
                               intermediateClass=UserLecture, entriesAmount=entriesAmount)
    return render_template('create.html', model=my_class, fkVars=fkVarsDict)

app = Flask(__name__)


@app.route('/edit/users/<int:element_id>/<int:entriesAmount>', methods=('GET', 'POST'))
def editMult(element_id, entriesAmount):
    table_name = "users"
    my_class = classAdresses[table_name]  # classAdresses mapping should be defined
    requestedClasses = connected_classes(my_class)  # connected_classes function should be defined
    fkVarsDict = {}

    for Class in requestedClasses:
        fkVarsDict.update(
            {Class.__name__: meaningfulClassValues(Class)})  # meaningfulClassValues function should be defined

    requestedClassesMultiple = connected_classes(Lecture)  # Lecture class should be defined
    fkVarsDictMultiple = {}

    for Class in requestedClassesMultiple:
        fkVarsDictMultiple.update({Class.__name__: meaningfulClassValues(Class)})

    connection = get_db_connection()  # get_db_connection function should be defined

    if request.method == 'POST':
        values = []
        for attribute in my_class.attributes:
            values.append(request.form[str(attribute)])
        my_class.push(connection, element_id, *values)  # Assuming push method takes ID for update

        if my_class.table_name == "users":
            lecture_requests = []
            userlecture_requests = []
            for i in range(entriesAmount):
                lecture_data = [request.form.get(str(attribute) + str(i)) for attribute in Lecture.attributes]
                userlecture_data = [request.form.get(str(attribute) + str(i) + "int")
                                    for attribute in UserLecture.attributes
                                    if not isinstance(attribute, foreignKey)]
                lecture_requests.append(lecture_data)
                userlecture_requests.append(userlecture_data)

            for i in range(len(lecture_requests)):
                Lecture.push(connection, *lecture_requests[i])
                UserLecture.push(connection, *userlecture_requests[i], Lecture.last(connection), User.last(connection))

        connection.commit()
        connection.close()
        flash(f'{my_class.stringRepresentation} updated successfully!', 'success')
        return redirect(url_for('users'))  # replace 'users' with the name of route showing user list

    # These methods are assumed - replace them with the right method to fetch data
    existing_user = my_class.get(connection, element_id)
    existing_lectures = Lecture.get(connection, element_id)

    connection.close()

    if my_class.table_name == "users":
        return render_template('edit_multiple_files.html', model=my_class, fkVars=fkVarsDict,
                               multipleAddClass=Lecture, fkAddVars=fkVarsDictMultiple,
                               intermediateClass=UserLecture, entriesAmount=entriesAmount,
                               record=existing_user, lectures=existing_lectures)

    return render_template('edit.html', model=my_class, fkVars=fkVarsDict, record=existing_user)
