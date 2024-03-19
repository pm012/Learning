import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    user = "admin",
    password = "secret01", 
    database = "TestDB"
)

cursor = db.cursor()
cursor.execute("INSERT INTO TestDB.People(Name, Age, City) VALUES ('Jack',26, 'Sydney'), ('Maxi',32,'New York'), ('John', 36, 'Mexico') ")
db.commit()
db.close()