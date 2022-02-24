import numpy as np
import matplotlib.pyplot as plt
import mysql.connector
import numpy as np
import tkinter as tk
from tkinter import ttk
import os
from tkinter import *
from tkinter import filedialog
from tkinter import Tk, Listbox, Button

defaultin = 0
aintdefaultin = 0
mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="faceapp"
            )

print(mydb)
mycursor = mydb.cursor()
#
data={}

import tkinter as tk
from tkinter import ttk

def barchart():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="faceapp"
    )

    print(mydb)
    mycursor = mydb.cursor()
    #
    data = {}
    # sql = "select DISTINCT dyString,COUNT(name) FROM attendance GROUP BY dyString"
    # val = (name, dtString, dyString)
    # mycursor.execute(sql, val)
    # mydb.commit()
    # mycursor = mydb.cursor()
    # print(mycursor.execute("select DISTINCT dyString,COUNT(name) FROM attendance GROUP BY dyString"))

    mycursor.execute("select DISTINCT dyString,COUNT(name) FROM attendance GROUP BY dyString")
    myresult = mycursor.fetchall()
    for x in myresult:
      temp={x[0]:x[1]}
      data.update(temp)
      print(x[1])

    datelist = list(data.keys())
    studentlist = list(data.values())

    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(datelist, studentlist, color='maroon',
            width=0.2)

    plt.xlabel("Date")
    plt.ylabel("No. of Students")
    plt.title("Daily Attendance")
    plt.show()


def close_windows():
    scores.destroy()

def goback():
    os.system('python dashboard.py')

def piechart():
    File_object = open(r"chartdata.txt", "r")

    count = 0

    while True:
        count += 1

        # Get next line from file
        line = File_object.readline()

        # if line is empty
        # end of file is reached
        if not line:
            break
        print("Line{}: {}".format(count, line.strip()))
        if count==1:
            defaultin=line

        elif count==2:
            aintdefaultin=line

    print(defaultin)
    print(aintdefaultin)


    File_object.close()
    # defaultin=File_object.readline()

    y = np.array([defaultin,aintdefaultin])
    mylabels = ["Defaulters"+defaultin,"Attenders ="+aintdefaultin]

    plt.pie(y, labels=mylabels)
    plt.show()

def individualreports():
    nameEnt = nameEntered.get()
    listbox1.delete(0, 'end')

    print(nameEnt)

    # mycursor.execute("\SELECT * FROM attendance WHERE name=%s")
    query = "SELECT * FROM attendance WHERE name='" + nameEnt + "'"


    # sql = "SELECT * FROM attendance WHERE name='%s"
    # val = nameEnt                                                    #OLD STUFF DONT UNCOMMENT
    # print(mycursor.execute(query))


    mycursor.execute(query)
    myresult = mycursor.fetchall()
    count = 1

    # listbox1.insert(1, "10-12-12")

    for x in myresult:
        print(x[2])

        listbox1.insert(count, x[2])

        count=count+1

        # i = 0
        # listbox1.insert(i, x[2])
        # i = i + 1
    # i = 1
    # listbox1.insert(i, "10-12-12")
    # i = i + 1



def show():
    mycursor.execute("select COUNT(DISTINCT dyString) FROM attendance")
    myresult2 = mycursor.fetchall()
    templist=[]
    for y in myresult2:
        print(y[0])

    mycursor.execute("select name, count(*) as c FROM attendance GROUP BY name")
    myresult = mycursor.fetchall()
    for x in myresult:
        temp = {x[0]: x[1]}
        data.update(temp)
        print(x[0], x[1])
        temp = x[1]
        percentage=((temp/ y[0]) * 100)

        templist.append([x[0],x[1],percentage])

    # tempList = [['Jim', '0.33'], ['Dave', '0.67'], ['James', '0.67'], ['Eden', '0.98']]
    defaultin=0
    aintdefaultin=0
    templist.sort(key=lambda e: e[1], reverse=True)
    print(templist)
    for i, (name, score, percent) in enumerate(templist, start=1):
        if percent<50:
            listBox.insert("", "end", values=(i, name, (score, "/", y[0]), (percent, "%"),("X")))
            defaultin=defaultin+1
        else:
            listBox.insert("", "end", values=(i, name, (score,"/",y[0]), (percent,"%"),("✓")))
            aintdefaultin=aintdefaultin+1

    File_object = open(r"chartdata.txt", "w")
    File_object.write(str(defaultin))
    File_object = open(r"chartdata.txt", "a")
    File_object.write("\n"+str(aintdefaultin))






scores = tk.Tk()
label = tk.Label(scores, text="ATTENDANCE OVERVIEW", font=("Arial",30)).grid(row=0, columnspan=3)
# create Treeview with 3 columns
cols = ('S.No','Name', 'Classes Attended', 'Atendance Percentage','Regular Student')
listBox = ttk.Treeview(scores, columns=cols, show='headings')
# set column headings
for col in cols:
    listBox.heading(col, text=col)
listBox.grid(row=1, column=0, columnspan=2)



show()
print(defaultin)
showScores = tk.Button(scores, text="BARCHART OVERVIEW", width=20, command=barchart).grid(row=5, column=1)
showpie = tk.Button(scores, text="PIECHART OVERVIEW", width=20, command=piechart).grid(row=6, column=1)

# closeButton = tk.Button(scores, text="Close", width=15, command=lambda: [close_windows(), goback()]).grid(row=4, column=1)
closeButton = tk.Button(scores, text="Close", width=15, command=lambda: [close_windows(), goback()]).grid(row=4, column=1)
findname = tk.StringVar()

nameEntered = ttk.Entry(scores, width=30, textvariable=findname)
nameEntered.grid(row=4, column = 0)
searchbtn = tk.Button(scores, text="Search", command=individualreports,borderwidth=2).grid(row=5, column=0)
listbox1 = Listbox(scores, height=20, width=20)
listbox1.grid(row=8,column=0)
scores.mainloop()

