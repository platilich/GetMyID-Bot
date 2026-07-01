import sqlite3

from record_log import log_info, log_error
from datetime import datetime, timedelta, timezone

DB_FILE = 'Users.db'



def get_current_time():
    return datetime.now().astimezone()



def initialize_database():
    try:
        log_info('Initializing database')

        con = sqlite3.connect('Users.db')
        cursor = con.cursor()


        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS Users (
                ID INTEGER PRIMARY KEY,
                name TEXT,
                username TEXT,
                count_message INTEGER,
                registrate DATETIME DEFAULT CURRENT_TIMESTAMP,
                last_message DATETIME
            )
            '''
        )

        log_info('Database successfully initialized')


    except Exception as e:
        log_error(f"Error initializing database: {e}")



def add_or_update_user(ID, name, username):
    try:
        log_info(f'Updating/adding user {ID}')


        con = sqlite3.connect('Users.db')
        cursor = con.cursor()



        now = datetime.now().astimezone()


        cursor.execute('SELECT ID FROM Users WHERE ID = ?', (ID,))
        user = cursor.fetchone()


        if user is None: # если пользователя нет
            cursor.execute('''INSERT INTO Users (ID, name, username, count_message, registrate, last_message) VALUES (?, ?, ?, ?, ?, ?) ''', (ID, name, username, 0, now, now))


        else: # если пользователь есть обновляем информацию
            cursor.execute('''UPDATE Users SET name = ?, username = ?, last_message = ? WHERE ID = ? ''', (name, username, now, ID))


        con.commit()
        con.close()


        log_info(f'User {ID} successfully updated/added')



    except Exception as e:
        log_error(f'Error adding/updating user {ID}: {e}')
        print(e)




def update_count_message(ID):
    con = sqlite3.connect('Users.db')
    cursor = con.cursor()


    cursor.execute('UPDATE Users SET count_message = count_message + 1 WHERE ID = ?', (ID, ))


    con.commit()
    con.close()






initialize_database()