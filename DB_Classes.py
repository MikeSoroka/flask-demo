class Meta(type):
    def __new__(cls, name, bases, attrs):
        attrs['table_name'] = name.upper() + "S"
        return super().__new__(cls, name, bases, attrs)

class DB_class(metaclass=Meta):
    id = "id"
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
      attributes = ("name", "surname", "country", "gender")
#     """
#     @staticmethod
#     def push(db_connection, id, name, surname, country, gender):
#         db_connection.execute('INSERT INTO users (id, name, surname, country, gender) VALUES (?, ?, ?, ?, ?)',
#                      (id, name, surname, country, gender))
#     @staticmethod
#     def select(db_connection, amount = "*"):
#         users = db_connection.execute('SELECT ? FROM users',
#                                       (str(amount))).fetchall()
#         return users
#     """
#     @staticmethod
#     def update(db_connection, id, name, surname, country, gender):
#         db_connection.execute('UPDATE users SET name = ?, surname = ?, country = ?, gender = ? WHERE id = ?',
#                               (name, surname, country, gender, id))
#     @staticmethod
#     def delete(db_connection, id):
#         db_connection.execute('DELETE FROM users WHERE id = ?', (id,))
#     @staticmethod
#     def get(db_connection, id):
#         return db_connection.execute('SELECT 1 FROM users WHERE id = ?', (id,)).fetchone()
#
# #class paymentMethod -> card_number, cvv_code, holder_name, card_name, paying_system, id, fk_USERid
# #class course -> id, name, approximate_duration, overview, price
# #class userCourse -> is_completed, fk_COURSEid, fk_USERid, id