import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '12345'
)

#Creating DATABASE and Check kung mogana
cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE crud")

print("GANA PLEASE :(")
