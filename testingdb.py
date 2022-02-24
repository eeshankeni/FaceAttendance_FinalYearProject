import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="faceapp"
)
print(mydb)
mycursor = mydb.cursor()

mycursor.execute("select name, count(*) as c FROM attendance GROUP BY name")
myresult = mycursor.fetchall()

for x in myresult:
  print(x[0],x[1])
  query = "INSERT INTO studentinfo('totalattended') VALUES (%s)"
  val =x[1]
  mycursor.execute(query,val)
  print("success")

mydb.commit()