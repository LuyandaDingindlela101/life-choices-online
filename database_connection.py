import mysql.connector

my_db = mysql.connector.connect(user='sql10423065', password='LGq9PVR277', host='sql10.freesqldatabase.com', database='sql10423065', auth_plugin='mysql_native_password')


#   ID_NUMBER AND PHONE_NUMBER MUST BE A STRING
def create_visitors_table():
    query = "CREATE TABLE visitors ( " \
            "id int unsigned NOT NULL auto_increment, " \
            "name varchar(50) NOT NULL, " \
            "surname varchar(50) NOT NULL, " \
            "id_number varchar(13) NOT NULL, " \
            "phone_number varchar(10) NOT NULL, " \
            "logged_in tinyint NOT NULL, " \
            "time_in varchar(50) NOT NULL, " \
            "time_out varchar(50) DEFAULT 'null' NOT NULL, " \
            "PRIMARY KEY (id) ); "

    my_cursor = my_db.cursor()
    my_cursor.execute(query)

    my_db.commit()


# MAKE VISITOR ID FOREIGN KEY
def create_admins_table():
    #     IF THE TABLE DOESNT EXIST, CREATE IT
    query = "CREATE TABLE admins ( " \
            "id int unsigned NOT NULL auto_increment, " \
            "name varchar(50) NOT NULL, " \
            "email varchar(50) NOT NULL, " \
            "password varchar(50) NOT NULL, " \
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
            "FOREIGN KEY (visitor_id) REFERENCES visitors(id) ); "

    my_cursor = my_db.cursor()
    my_cursor.execute(query)


def insert_visitor(name, surname, id_number, phone_number, logged_in, time_in):
    query = "INSERT INTO visitors ( name ,surname ,id_number ,phone_number ,logged_in ,time_in ) " \
            "VALUES ( '" + name + "', '" + surname + "', '" + id_number + "', '" + phone_number + "', '" + str(logged_in) + "', '" + time_in + "' );"

    my_cursor = my_db.cursor()
    my_cursor.execute(query)

    my_db.commit()


def insert_nok(name, phone_number, visitor_id):
    query = "INSERT INTO next_of_kin ( name ,phone_number, visitor_id ) " \
            "VALUES ( '" + name + "', '" + phone_number + "', '" + str(visitor_id) + "' );"

    my_cursor = my_db.cursor()
    my_cursor.execute(query)

    my_db.commit()

def insert_admin(name, email, password):
    query = "INSERT INTO admins ( name ,email ,password ) " \
            "VALUES ( '" + name + "', '" + email + "', '" + password + "' );"

    my_cursor = my_db.cursor()
    my_cursor.execute(query)

    my_db.commit()

def read_table(table_name):
    my_cursor = my_db.cursor()
    my_cursor.execute('SELECT * FROM ' + table_name)

    for i in my_cursor:
        print(i)


def describe_table(table_name):
    my_cursor = my_db.cursor()
    my_cursor.execute('DESCRIBE ' + table_name)

    for i in my_cursor:
        print(i)


def show_tables():
    my_cursor = my_db.cursor()
    my_cursor.execute('SHOW TABLES')

    for i in my_cursor:
        print(i)


def drop_table(table_name):
    my_cursor = my_db.cursor()
    my_cursor.execute('DROP TABLE ' + table_name)
