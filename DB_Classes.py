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

    # TODO: Change class methods to normal ones
    # TODO: make self.attributes be elements of data_entries.Column 
    # TODO: Create assertion for ensuring column types are the same as in DB


    def __init__(self, db_connection, table_name, id_column_name, string_representation, attributes):
        self.db_connection = db_connection
        self.table_name = table_name
        self.id_column = id_column_name
        self.string_representation = string_representation
        self.attributes = attributes


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

    @classmethod
    def last(cls, db_connection):
        return db_connection.execute(f'''SELECT * FROM {cls.table_name} 
                                         WHERE {cls.id}=(SELECT max({cls.id})
                                         FROM {cls.table_name})''').fetchone()[0]
    
    def add_column(self, column_name, column_type):
        try:
            self.db_connection.execute(f'''ALTER TABLE {self.table_name}
                                           ADD COLUMN {column_name} {column_type}''')
            return True
        except:
            print(f"Failed to create {column_type} column {column_name} in table {cls.table_name}")
            return False
        
    def drop_column(self, column_name):
        try:
            self.db_connection.execute(f'''ALTER TABLE {self.table_name}
                                           DROP COLUMN {column_name}''')
            return True
        except:
            print(f"Failed to drop column {column_name} in table {self.table_name}")
            return False
        
    def rename_column(self, column_name, new_name):
        try:
            self.db_connection.execute(f'''ALTER TABLE {self.table_name}
                                           RENAME COLUMN {column_name} to {new_name}''')
            return True
        except:
            print(f"Failed to rename column {column_name} to {new_name} in table {self.table_name}")
            return False
        
    def alter_column(self, column_name, new_type):
        try:
            self.db_connection.execute(f'''ALTER TABLE {self.table_name}
                                           ALTER COLUMN {column_name} {new_type}''')
            return True
        except:
            print(f"Failed to alter column {column_name} type to {new_type} in table {self.table_name}")
            return False
        
    def get_pragma(self, pragma_name):
        try:
            fragma = self.db_connection.execute(f"PRAGMA {pragma_name}({self.table_name})")
            return fragma.fetchall()
        except:
            print(f"Failed to get PRAGMA {pragma_name} for table {self.table_name}")
    
    def get_column_type(self, column_name):
        if(column_name in self.attributes):
            columns_info = self.get_pragma("table_info")
            for column_info in columns_info: # column_info is array with column data. column name has index [1] and column type [2]
                if column_info[1] == column_name:
                    return column_info[2]
            print(f"Unexpected error in {self.table_name}.get_column_type({column_name}) happened!")
            return
        else:
            print(f"Failed to get column type. Column {column_name} doesnt exists in {self.table_name}")
            return


class Gender(DB_class):
    table_name = "genders"
    stringRepresentation = "Gender"
    attibutes = ("gender",)

class User(DB_class):
    table_name = "users"
    stringRepresentation = "User"
    attributes = ("name", "surname", "country",
                foreignKey("fk_GENDERid", Gender))
#user's amount of lectures in a given course
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
                "start_date",
                foreignKey("fk_LECTUREid", Lecture),
                foreignKey("fk_USERid", User))

