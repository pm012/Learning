import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="admin", 
    password="secret01",
    database="TestDB"
)

cursor = db.cursor()
#cursor.execute("CREATE TABLE People (Name varchar(50), Age int, City varchar(50))")
cursor.execute("CREATE TABLE ProgrammingHub (category varchar(255), duration varchar(255), level varchar(255))")
db.commit()
cursor.close()
db.close()