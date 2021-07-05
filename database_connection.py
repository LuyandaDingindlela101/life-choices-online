import mysql.connector

my_db = mysql.connector.connect(user='sql10423065', password='LGq9PVR277', host='sql10.freesqldatabase.com',
                                database='sql10423065', auth_plugin='mysql_native_password')


def create_visitors_table():
    query = "CREATE TABLE visitors ( " \
            "id int unsigned NOT NULL auto_increment, " \
            "name varchar(50) NOT NULL, " \
            "surname varchar(50) NOT NULL, " \
            "id_number int NOT NULL, " \
            "phone_number int NOT NULL, " \
            "nok_id int unsigned NOT NULL, " \
            "logged_in tinyint NOT NULL, " \
            "time_in datetime NOT NULL, " \
            "time_out datetime NOT NULL, " \
            "PRIMARY KEY (id), " \
            "FOREIGN KEY (nok_id) REFERENCES next_of_kin(id) ); "

    my_cursor = my_db.cursor()
    my_cursor.execute(query)


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


def create_nok_table():
    #     IF THE TABLE DOESNT EXIST, CREATE IT
    query = "CREATE TABLE next_of_kin ( " \
            "id int unsigned NOT NULL auto_increment, " \
            "name varchar(50) NOT NULL, " \
            "phone_number int NOT NULL, " \
            "PRIMARY KEY (id) ); "

    my_cursor = my_db.cursor()
    my_cursor.execute(query)


def read_database():
    my_cursor = my_db.cursor()
    my_cursor.execute('SELECT * FROM visitors')

    for i in my_cursor:
        print(i)


def describe_database():
    my_cursor = my_db.cursor()
    my_cursor.execute('DESCRIBE visitors')

    for i in my_cursor:
        print(i)


def show_tables():
    my_cursor = my_db.cursor()
    my_cursor.execute('SHOW TABLES')

    for i in my_cursor:
        print(i)


# def drop_table():
#     my_cursor = my_db.cursor()
#     my_cursor.execute('DROP TABLE visitors')



show_tables()
