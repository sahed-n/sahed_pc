import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '$ql!180723#^'
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#creare a database
cursorObject.execute("CREATE DATABASE biblio_db")

print("DB creation all good")