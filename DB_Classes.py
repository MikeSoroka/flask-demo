class user():
    @staticmethod
    def push(db_connection, id, name, surname, country, gender):
        db_connection.execute('INSERT INTO users (id, name, surname, country, gender) VALUES (?, ?, ?, ?, ?)',
                     (id, name, surname, country, gender))
    @staticmethod
    def get(db_connection, amount = "*"):
        users = db_connection.execute('SELECT ? FROM posts',
                                      (str(amount))).fetchall()
        return users


#class paymentMethod -> card_number, cvv_code, holder_name, card_name, paying_system, id, fk_USERid
#class course -> id, name, approximate_duration, overview, price
#class userCourse -> is_completed, fk_COURSEid, fk_USERid, id