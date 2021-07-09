import mysql.connector
from duplicity.dup_time import curtime

my_db = mysql.connector.connect(user='sql10423065', password='LGq9PVR277', host='sql10.freesqldatabase.com', database='sql10423065', auth_plugin='mysql_native_password')


#   ID_NUMBER AND PHONE_NUMBER MUST BE A STRING
def create_visitor_table():
    query = "CREATE TABLE visitor ( " \
            "id int unsigned NOT NULL auto_increment, " \
            "name varchar(50) NOT NULL, " \
            "surname varchar(50) NOT NULL, " \
            "id_number varchar(13) NOT NULL, " \
            "phone_number varchar(10) NOT NULL, " \
            "logged_in tinyint NOT NULL, " \
            "time_in time NOT NULL, " \
            "time_out time NOT NULL, " \
            "PRIMARY KEY (id) ); "

    my_cursor = my_db.cursor()
    my_cursor.execute(query)

    my_db.commit()


# MAKE VISITOR ID FOREIGN KEY
def create_admin_table():
    #     IF THE TABLE DOESNT EXIST, CREATE IT
    query = "CREATE TABLE admin ( " \
            "id int unsigned NOT NULL auto_increment, " \
            "name varchar(50) NOT NULL, " \
            "email varchar(50) NOT NULL, " \
            "id_number varchar(13) NOT NULL, " \
            "PRIMARY KEY (id) ); "

    my_cursor = my_db.cursor()
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

    my_cursor = my_db.cursor()
    my_cursor.execute(query)


def insert_visitor(name, surname, id_number, phone_number):
    #   logged_in WILL HAVE ONLY TWO VALUES: 1 AND 0, 1 MEANS LOGGED IN AND 0 MEANS LOGGED OUT
    query = "INSERT INTO visitor ( name ,surname ,id_number ,phone_number ,logged_in ,time_in ) " \
            "VALUES ( '" + name + "', '" + surname + "', '" + id_number + "', '" + phone_number + "', '" + 1 + "', '" + curtime() + "' );"

    my_cursor = my_db.cursor()
    my_cursor.execute(query)

    my_db.commit()


def insert_nok(name, phone_number, visitor_id):
    query = "INSERT INTO next_of_kin ( name ,phone_number, visitor_id ) " \
            "VALUES ( '" + name + "', '" + phone_number + "', '" + str(visitor_id) + "' );"

    my_cursor = my_db.cursor()
    my_cursor.execute(query)

    my_db.commit()


def insert_admin(name, email, id_number):
    query = "INSERT INTO admin ( name, email, id_number ) " \
            "VALUES ( '" + name + "', '" + email + "', '" + id_number + "' );"

    my_cursor = my_db.cursor()
    my_cursor.execute(query)

    my_db.commit()


def update_table(query):
    my_cursor = my_db.cursor()
    my_cursor.execute(query)

    my_db.commit()


def delete_entry(table_name, column_name, id):
    query = "DELETE FROM " + table_name + " WHERE " + column_name + " = " + id + ";"

    my_cursor = my_db.cursor()
    my_cursor.execute(query)

    my_db.commit()


def read_table(table_name):
    my_cursor = my_db.cursor()
    my_cursor.execute('SELECT * FROM ' + table_name)

    return my_cursor.fetchall()


def describe_table(table_name):
    my_cursor = my_db.cursor()
    my_cursor.execute('DESCRIBE ' + table_name)

    for i in my_cursor:
        print(i)


def show_tables():
    my_cursor = my_db.cursor()
    my_cursor.execute('SHOW TABLES')

    return my_cursor.fetchall()


def drop_table(table_name):
    my_cursor = my_db.cursor()
    my_cursor.execute('DROP TABLE ' + table_name)


def select_from_table(query):
    my_cursor = my_db.cursor()
    my_cursor.execute(query)

    return my_cursor.fetchall()
