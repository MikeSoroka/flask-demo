from DB_Classes import *
import sqlite3

connection = sqlite3.connect("database.db")
connection.row_factory = sqlite3.Row
c = connection.cursor()

id = c.execute(f'SELECT * FROM user_lectures WHERE id=(SELECT max(id) '
                                 f'FROM user_lectures)').fetchone()[0]

c.execute(f'DELETE FROM user_lectures WHERE id = ?', (int(id),))




connection.commit()
connection.close()