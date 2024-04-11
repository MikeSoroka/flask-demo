class Meta(type):
    def __new__(cls, name, bases, attrs):
        attrs['table_name'] = name.upper() + "S"
        return super().__new__(cls, name, bases, attrs)

class DB_class(metaclass=Meta):
    id = "id"
    attributes = ()
    @classmethod
    def push(DB_connection, **all_attributes):
        DB_connection.execute('INSERT INTO ? ? VALUES ?',
                              (DB_class.table_name, str(DB_class.attributes), str(tuple(all_attributes))))

    @classmethod
    def select(cls, db_connection, amount=None):
        query = f"SELECT * FROM '{cls.table_name}'"
        if amount is not None:
            query += " LIMIT ?"
            users = db_connection.execute(query, (amount,))
        else:
            users = db_connection.execute(query)
        return users.fetchall()
"""
    @staticmethod
    def update(db_connection, id, **non_id_attributes):
        db_connection.execute('UPDATE ? SET ? WHERE ? = ?',
                              (BD_class.table_name, str(tuple()), surname, country, gender, id))

    @staticmethod
    def delete(db_connection, id):
        db_connection.execute('DELETE FROM users WHERE id = ?', (id,))

    @staticmethod
    def get(db_connection, id):
        return db_connection.execute('SELECT 1 FROM users WHERE id = ?', (id,)).fetchone()
"""

class user(DB_class):

    def __init__(self):
        super().__init__()
        user.attributes = ("id", "name", "surname", "country", "gender")
    """
    @staticmethod
    def push(db_connection, id, name, surname, country, gender):
        db_connection.execute('INSERT INTO users (id, name, surname, country, gender) VALUES (?, ?, ?, ?, ?)',
                     (id, name, surname, country, gender))
    @staticmethod
    def select(db_connection, amount = "*"):
        users = db_connection.execute('SELECT ? FROM users',
                                      (str(amount))).fetchall()
        return users
    """
    @staticmethod
    def update(db_connection, id, name, surname, country, gender):
        db_connection.execute('UPDATE users SET name = ?, surname = ?, country = ?, gender = ? WHERE id = ?',
                              (name, surname, country, gender, id))
    @staticmethod
    def delete(db_connection, id):
        db_connection.execute('DELETE FROM users WHERE id = ?', (id,))
    @staticmethod
    def get(db_connection, id):
        return db_connection.execute('SELECT 1 FROM users WHERE id = ?', (id,)).fetchone()

#class paymentMethod -> card_number, cvv_code, holder_name, card_name, paying_system, id, fk_USERid
#class course -> id, name, approximate_duration, overview, price
#class userCourse -> is_completed, fk_COURSEid, fk_USERid, id