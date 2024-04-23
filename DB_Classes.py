# class Meta(type):
#     def __new__(cls, name, bases, attrs):
#         attrs['table_name'] = name.upper() + "S"
#         return super().__new__(cls, name, bases, attrs)

class DB_class():
    id = "id"
    table_name = ""
    attributes = ()

    @classmethod
    def push(cls, DB_connection, *non_id_attributes):
        placeholders = ', '.join('?' * len(non_id_attributes))
        attributes = ', '.join(cls.attributes)
        query = f'INSERT INTO {cls.table_name} ({attributes}) VALUES ({placeholders})'
        DB_connection.execute(query, tuple(non_id_attributes))

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

class User(DB_class):
    table_name = "users"
    attributes = ("name", "surname", "country", "gender")


class PaymentMethod(DB_class):
    table_name = "payment_methods"
    attributes = ("card_number", "cvv_code", "holder_name", "card_name", "paying_system", "fk_USERid")


class Course(DB_class):
    table_name = "courses"
    attributes = ("name", "approximate_duration", "overview", "price")


class UserCourse(DB_class):
    table_name = "user_courses"
    attributes = ("is_completed", "fk_COURSEid", "fk_USERid")