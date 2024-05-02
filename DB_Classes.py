# class Meta(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['table_name'] = name.upper() + "S"
#         return super().__new__(cls, name, bases, attrs)
from data_entries import *


class DB_class():
    id = "id"
    table_name = ""
    stringRepresentation = ""
    attributes = ()

    @classmethod
    def push(cls, DB_connection, *non_id_attributes):
        placeholders = ', '.join('?' * len(non_id_attributes))
        attributes = ', '.join((str(i) for i in cls.attributes))
        query = f'INSERT INTO {cls.table_name} ({attributes}) VALUES ({placeholders})'
        DB_connection.execute(query, tuple(str(i) for i in non_id_attributes))

    @classmethod
    def select(cls, db_connection, amount=None):
        query = f"SELECT * FROM '{cls.table_name}'"
        if amount is not None:
            query += " LIMIT ?"
            users = db_connection.execute(query, (amount,))
        else:
            users = db_connection.execute(query)
        return users.fetchall()
    @classmethod
    def update(cls, db_connection, id, *non_id_attributes):
        placeholders = ['?'] * len(non_id_attributes)
        prompt = ', '.join([f"{i} = {j}" for i, j in zip(cls.attributes, placeholders)])
        db_connection.execute(f'UPDATE {cls.table_name} SET {prompt} WHERE {cls.id} = ?',
                              non_id_attributes + (id,))

    @classmethod
    def delete(cls, db_connection, id):
        db_connection.execute(f'DELETE FROM {cls.table_name} WHERE {cls.id} = ?', (id,))

    @classmethod
    def get(cls, db_connection, id):
        return db_connection.execute(f'SELECT * FROM {cls.table_name} WHERE {cls.id} = ?', (id,)).fetchone()

class Gender(DB_class):
    table_name = "genders"
    stringRepresentation = "Gender"
    attibutes = ("gender",)

class User(DB_class):
    table_name = "users"
    stringRepresentation = "User"
    attributes = ("name", "surname", "country",
                  foreignKey("fk_GENDERid", Gender))

class Course(DB_class):
    table_name = "courses"
    stringRepresentation = "Course"
    attributes = ("name", "approximate_duration", "overview", "price")

class Lecture(DB_class):
    table_name = "lectures"
    stringRepresentation = "Lecture"
    attributes = ("title",
                  foreignKey("fk_COURSEid", Course))

class UserLecture(DB_class):
    table_name = "user_lectures"
    stringRepresentation = "User Lecture"
    attributes = (limitedVariantsDataEntry("is_completed", (0, 1)),
                  limitedVariantsDataEntry("is_starred", (0,1)),
                  foreignKey("fk_LECTUREid", Lecture),
                  foreignKey("fk_USERid", User))

