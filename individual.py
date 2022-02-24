# individual person reports
import mysql.connector
from tkinter import *
import tkinter as tk
from PIL import Image
from PIL import ImageTk
import os
import threading

root = Tk()
root.geometry("500x400")
root.title("Individual Attendance")
p1 = PhotoImage(file='appicon.png')
root.iconphoto(False, p1)
bgi = Image.open("Capture1.png")
bgi.image = bgi
bgi1 = bgi.resize((500, 400), Image.ANTIALIAS)
bgi2 = ImageTk.PhotoImage(bgi1)
canvas1 = Canvas(root, width=500, height=400)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bgi2, anchor="nw")


def check_quarry_thread():
    os.system('python Get_Individual_Quarry.py')


my_str = tk.StringVar()
l1 = tk.Label(root,  textvariable=my_str, width=10).place()


def show_lan(my_language):
    my_str.set(my_language)
    t2 = threading.Thread(target=check_quarry_thread)
    t2.start()


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="faceapp"
)

names =[]
#get count of No. of students in DB
mycursor = mydb.cursor()
mycursor.execute("select DISTINCT COUNT(name) FROM attendance GROUP BY dyString")
ButtonCount = mycursor.fetchall()
for y in ButtonCount:
    print(y[0])

#get student names from DB
mycursor.execute("select DISTINCT name FROM attendance")
names = mycursor.fetchall()
i = 0
a = 0
for x in names:
    print(x[0])
    mybutton = Button(root, text="{}".format(x[0]), width=10, bg='#2CFF34', command=lambda lan=x[0]: show_lan(lan))
    button1_canvas = canvas1.create_window((210, 70 + a), anchor="nw", window=mybutton)
    # mybutton.place(x=210, y=70+a)
    i = i + 1
    a = a + 50


root.mainloop()