import json
import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from DB_Classes import *
from data_entries import *

app = Flask(__name__)

usersTitle = ["ID", "Name", "Surname", "Country", "Gender"]
lecturesTitle = ["ID", "Title", "Course"]
coursesTitle = ["ID", "Name", "Approximate duration", "Overview", "Price"]
userLecturesTitle = ["ID", "Is Completed", "Is Starred", "Start Date", "Lecture", "User"]
gendersTitle = ["ID", "Gender"]

classAdresses = {"users": User,
                 "courses": Course,
                 "lectures": Lecture,
                 "user_lectures": UserLecture,
                 "genders": Gender}




def lecturesByID(ID, db='database.db'):
    res = []
    connection = get_db_connection(db)
    userLectures = UserLecture.select(connection)
    for userLecture in userLectures:
        if userLecture["fk_USERid"] == ID:
            res.append(Lecture.get(connection, userLecture["fk_Lectureid"]))
    return res

def ULByIDs(userID, lectureID, db='database.db'):
    res = []
    connection = get_db_connection(db)
    userLectures = UserLecture.select(connection)
    for userLecture in userLectures:
        if userLecture["fk_USERid"] == userID and userLecture["fk_Lectureid"] == lectureID:
            return(Lecture.get(connection, userLecture["fk_Lectureid"]))
#return {}



def tableFkToDict(table_name, rows):
    if (table_name == "user_lectures"):
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
        genders_dict = fkToDict(foreignKey("fk_GENDERid", Gender), rows, "gender")
        return genders_dict

    elif (table_name == "courses"):
        return {}

    elif (table_name == "lectures"):
        courses_dict = fkToDict(foreignKey("fk_COURSEid", Course), rows, "name")
        return courses_dict


def meaningfulClassValues(table_class, db="database.db"):
    connection = get_db_connection()
    rows = table_class.select(connection)
    if (table_class.table_name == "users"):
        return {str(row["id"]): (row["name"] + " " + row["surname"]) for row in rows}

    elif (table_class.table_name == "courses"):
        return {str(row["id"]): row["name"] for row in rows}

    elif (table_class.table_name == "lectures"):
        return {str(row["id"]): row["title"] for row in rows}

    elif (table_class.table_name == "genders"):
        return {str(row["id"]): row["gender"] for row in rows}


def idListByClass(className, db='database.db'):  # type:(str, str) -> list
    res = []
    connection = get_db_connection(db)
    currentClass = classAdresses[className]
    for row in currentClass.select(connection):
        res.append(row[currentClass.id])
    return res


def idListByFK(FK, db='database.db'):  # type:(foreignKey, str) -> list
    res = []
    connection = get_db_connection(db)
    currentClass = FK.Class
    for row in currentClass.select(connection):
        res.append(row[currentClass.id])
    return res


def fkToDict(FK, rows, corresponding_attribute, db='database.db'):
    res = {}
    res.update({FK: {}})
    connection = get_db_connection(db)
    for row in rows:
        ID = row[str(FK)]
        try:
            (res[FK].update
             ({ID: FK.Class.get(connection, ID)[corresponding_attribute]}))
        except TypeError:
            print("No such attribute")
    return res


# transforms string of type <smth>s to <SMTH>
def tableNameToClassName(link):
    return link[:-1].upper()


def get_db_connection(db='database.db'):
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


@app.template_filter('getL')
def getL(usID):
    res = []
    connection = get_db_connection()
    ULs = UserLecture.select(connection)
    for ul in ULs:
        if str(ul["fk_USERid"]) == str(usID):
            res.append(ul["fk_USERid"])
    return res

@app.template_filter('connectedToFK')
def connected(FK):
    return idListByFK(FK)


@app.template_filter('attributeType')
def attributeType(attribute):
    if isinstance(attribute, limitedVariantsDataEntry):
        return "M"
    if isinstance(attribute, foreignKey):
        return "FK"
    return "C"


@app.template_filter('str')
def toString(value):
    return str(value)

@app.template_filter('len')
def length(value):
    return len(value)

@app.template_filter('int')
def toInt(value):
    return int(value)

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
    # foreignKey("fk_USERid", User))
    if isinstance(my_class, User):
        return render_template('users.html', rows=rows, table_class=my_class,
                           special_attributes=tableFkToDict(my_class.table_name, rows))
    return render_template('table.html', rows=rows, table_class=my_class,
                           special_attributes=tableFkToDict(my_class.table_name, rows))


@app.route('/create/<string:table_name>', methods=('GET', 'POST'))
# those lines post all required data in user and rendering create.html
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
# those lines post all required data in user and rendering create.html
def edit(table_name, element_id):
    connection = get_db_connection()
    my_class = classAdresses[table_name]
    requestedClasses = connected_classes(my_class)
    record = my_class.get(connection, element_id)
    fkVarsDict = {}
    for Class in requestedClasses:
        fkVarsDict.update({Class: meaningfulClassValues(Class)})
    if request.method == 'POST':
        values = []
        # values[my_class.id] = request.form.get('id')
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


@app.route('/report', methods=('GET', 'POST'))
def report():
    table_name = "users"
    connection = get_db_connection()
    cursor = connection.cursor()
    data = cursor.execute("""
        SELECT users.id, users.name, users.surname, users.country, genders.gender, lectures.title
            FROM users
            LEFT JOIN lectures
            ON lectures.id IN
               (SELECT fk_LECTUREid
                FROM user_lectures
                WHERE fk_USERid = users.id)
            LEFT JOIN genders
            ON genders.id = users.fk_GENDERid

        GROUP BY users.id, lectures.id
        ORDER BY users.id
    """).fetchall()
    #data.fetchall()
    for row in data:
        for key in row:
            print(key)


    my_class = classAdresses[table_name]
    rows = my_class.select(connection)
    special_attributes = {}
    # foreignKey("fk_USERid", User))
    if request.method == 'POST':
        values = []
        for attribute in ["is_completed", "is_starred", "age"]:
            values.append(str(request.form[attribute]))

        connection = get_db_connection()
        cursor = connection.cursor()
        data = cursor.execute("""
            SELECT
                users.id,
                users.name,
                users.surname,
                users.country,
                genders.gender,
                courses.name AS course,
                COUNT(lectures.id) AS total_lectures,
                CAST(ROUND(AVG(CASE WHEN ul.is_completed = ? THEN 1 ELSE 0 END) * 100, 1) AS TEXT) || '%' AS completion_rate,
                CAST(ROUND(AVG(CASE WHEN ul.is_starred = ? THEN 1 ELSE 0 END) * 100, 1)AS TEXT) || '%' AS star_rate,
                COUNT(CASE WHEN strftime('%Y', ul.start_date) = ? THEN 1 ELSE NULL END) AS lecture_years_count
            FROM
                users
            LEFT JOIN
                user_lectures ul ON ul.fk_USERid = users.id
            LEFT JOIN
                lectures ON lectures.id = ul.fk_LECTUREid
            LEFT JOIN
                courses ON courses.id = lectures.fk_COURSEid
            LEFT JOIN
                genders ON genders.id = users.fk_GENDERid
                GROUP BY
                    users.id,
                    courses.id
            ORDER BY
                users.id;

        """, tuple(values)).fetchall()
        return render_template('submitted_report.html', rows=data, table_class=my_class)

    return render_template('report.html', rows=data, table_class=my_class)