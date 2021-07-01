import mysql.connector

my_db = mysql.connector.connect(user='epiz_29025234', password='ldke7M8igIbjSrB', host='sql303.epizy.com', database='epiz_29025234_XXX', auth_plugin='mysql_native_password')


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


read_database()