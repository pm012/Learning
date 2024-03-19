import mysql.connector
db_connection = mysql.connector.connect(
    host = 'localhost',
    user = 'admin',
    password = 'secret01',
    database = 'TestDB'
)

my_database = db_connection.cursor()
sql_statement = "UPDATE ProgrammingHub SET duration='150 Hours' where category = 'Python' "
my_database.execute(sql_statement)
db_connection.commit()
my_database.close()
db_connection.close()