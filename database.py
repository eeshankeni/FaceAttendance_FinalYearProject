# import sqlite3
#
# name = "av"
# dtString = "11-10-1999"
# timeString = "10:10:20"
# conn = sqlite3.connect("faceapp.db")
#
# c = conn.cursor()
#
# # c.execute("INSERT INTO attendance VALUES (?,?,?)", (name, dtString, timeString))
# sql = "INSERT INTO attendance (name, dtString, timeString) VALUES (%s, %s, %s)"
# val = ("John", "Highway 21", "121")
# c.execute(sql, val)
# conn.commit()
#
# mydb.commit()
#
# print(mycursor.rowcount, "record inserted.")
#
#
#
# print(c.fetchall())
# conn.close()
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="faceapp"
)
print(mydb)
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE faceapp")
# mycursor.execute("CREATE TABLE attendance(name VARCHAR(255),dtString VARCHAR(255),dyString VARCHAR(255))")
sql = "INSERT INTO attendance (name, dtString, dyString) VALUES (%s, %s, %s)"
val = ("John", "Highway 21","12123")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


