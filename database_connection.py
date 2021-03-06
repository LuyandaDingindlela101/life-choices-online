import mysql.connector
from duplicity.dup_time import curtime


my_db = mysql.connector.connect(user='sql10423065', password='LGq9PVR277', host='sql10.freesqldatabase.com', database='sql10423065', auth_plugin='mysql_native_password')
my_cursor = my_db.cursor()


#   ID_NUMBER AND PHONE_NUMBER MUST BE A STRING
def create_visitor_table():
    query = "CREATE TABLE visitor ( " \
            "id int unsigned NOT NULL auto_increment, " \
            "name varchar(50) NOT NULL, " \
            "surname varchar(50) NOT NULL, " \
            "id_number varchar(13) NOT NULL, " \
            "phone_number varchar(10) NOT NULL, " \
            "is_admin varchar(10) DEFAULT 'false' NOT NULL, " \
            "logged_in varchar(10) DEFAULT 'false' NOT NULL, " \
            "time_in time NOT NULL, " \
            "time_out time NOT NULL, " \
            "PRIMARY KEY (id) ); "

    my_cursor.execute(query)
    my_db.commit()


def create_nok_table():
    query = "CREATE TABLE next_of_kin ( " \
            "id int unsigned NOT NULL auto_increment, " \
            "name varchar(50) NOT NULL, " \
            "phone_number varchar(10) NOT NULL, " \
            "visitor_id int unsigned NOT NULL, " \
            "PRIMARY KEY (id), " \
            "FOREIGN KEY (visitor_id) REFERENCES visitor(id) ); "

    my_cursor.execute(query)


def create_history_table():
    query = "CREATE TABLE history (" \
            "id int unsigned NOT NULL auto_increment, " \
            "visitor_id int unsigned NOT NULL, " \
            "timestamp_in datetime NOT NULL, " \
            "timestamp_out datetime NOT NULL, " \
            "PRIMARY KEY (id), " \
            "FOREIGN KEY (visitor_id) REFERENCES visitor(id) ); "

    my_cursor.execute(query)


def insert_visitor(name, surname, id_number, phone_number, admin_status, login_status):
    query = f"INSERT INTO visitor ( name ,surname ,id_number ,phone_number ,is_admin ,logged_in ,time_in ) " \
            f"VALUES ( '{name}', '{surname}', '{id_number}', '{phone_number}', '{admin_status}', '{login_status}', curtime() );"

    my_cursor.execute(query)
    my_db.commit()


def insert_nok(name, phone_number, visitor_id):
    query = f"INSERT INTO next_of_kin ( name ,phone_number, visitor_id ) " \
            f"VALUES ( '{name}', '{phone_number}', '{str(visitor_id)}' );"

    my_cursor.execute(query)
    my_db.commit()


def insert_history_in(visitor_id):
    query = f"INSERT INTO history ( visitor_id, timestamp_in ) VALUES({str(visitor_id)}, curdate())"

    my_cursor.execute(query)
    my_db.commit()


def insert_history_out(visitor_id):
    query = f"INSERT INTO history ( visitor_id, timestamp_out ) VALUES({str(visitor_id)}, curdate())"

    my_cursor.execute(query)
    my_db.commit()


def update_table(query):
    my_cursor.execute(query)
    my_db.commit()


def delete_entry(table_name, column_name, column_value):
    query = f"DELETE FROM {table_name} WHERE {column_name} = {column_value};"

    my_cursor.execute(query)
    my_db.commit()


def read_table(table_name):
    my_cursor.execute(f"SELECT * FROM {table_name}")
    return my_cursor.fetchall()


def describe_table(table_name):
    my_cursor.execute(f"DESCRIBE {table_name}")
    return my_cursor.fetchall()


def show_tables():
    my_cursor.execute('SHOW TABLES')
    return my_cursor.fetchall()


def drop_table(table_name):
    my_cursor.execute(f"DROP TABLE {table_name}")


def select_from_table(query):
    my_cursor.execute(query)
    return my_cursor.fetchall()
