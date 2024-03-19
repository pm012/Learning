import mysql.connector
db_connection = mysql.connector.connect(
    host = 'localhost',
    user = 'admin',
    password = 'secret01',
    database = 'TestDB'
)

my_database = db_connection.cursor()
sql_statement = "Select * FROM ProgrammingHub"
my_database.execute(sql_statement)
output = my_database.fetchall()
for x in output:
    print(x)
