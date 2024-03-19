import mysql.connector

db_connection = mysql.connector.connect(
    host = 'localhost',
    user = 'admin',
    password = 'secret01',
    database = 'TestDB'
    )


my_db = db_connection.cursor()
statement = "DELETE FROM ProgrammingHub where category = 'PHP'"
my_db.execute(statement)
db_connection.commit()
my_db.close()
db_connection.close()