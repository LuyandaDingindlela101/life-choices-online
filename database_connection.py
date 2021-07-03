import mysql.connector

my_db = mysql.connector.connect(user='epiz_29025234', password='ldke7M8igIbjSrB', host='sql303.epizy.com', database='epiz_29025234_XXX', auth_plugin='mysql_native_password')


def read_database():
    my_cursor = my_db.cursor()
    my_cursor.execute('SELECT * FROM visitors')

    for i in my_cursor:
        print(i)

#     IF THE TABLE DOESNT EXIST, CREATE IT
    query = "CREATE TABLE visitors ( " \
            "visitor_id int unsigned NOT NULL auto_increment, " \
            "visitor_name varchar(50) NOT NULL, " \
            "visitor_surname varchar(50) NOT NULL, " \
            "visitor_id_number int NOT NULL, " \
            "visitor_number int NOT NULL, " \
            "nok_name varchar(50) NOT NULL, " \
            "nok_number int NOT NULL, " \
            "logged_in tinyint NOT NULL, " \
            "time_in datetime NOT NULL, " \
            "time_out datetime NOT NULL, " \
            "PRIMARY KEY (visitor_id) ); "


def describe_database():
    my_cursor = my_db.cursor()
    my_cursor.execute('DESCRIBE visitors')

    for i in my_cursor:
        print(i)


read_database()