import face_recognition
from PIL import Image, ImageDraw
import cv2
import numpy as np

from PIL import ImageTk, Image
from datetime import datetime
import pickle
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import shutil,os
import os
import threading
from tkinter.ttk import Progressbar
import tkinter as tk
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="faceapp"
)
mycursor = mydb.cursor()

root2 = Tk()
root2.title("Edit Student")
root2.geometry("350x500")
p1 = PhotoImage(file='appicon.png')
root2.iconphoto(False, p1)

counter = 0
list_encoded_faces = []
list_encoded_names = []


#######################################   do encoding function   ################################################
def do_encodings(name):
    all_face_encodings = {}
    global my_image
    global counter
    global list_encoded_faces
    global list_encoded_names  # name list in def enternaem
    global listimages

    try:
        counter = counter + 1
        second_frame.filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(
        ("Image files", ".png",), ("Image files", ".jpg",), ("all files", ".")))
        print(second_frame.filename)
        sql="INSERT INTO studentinfo (name,totalattended, attendancepercent) VALUES (%s,%s,%s)"
        val = (name,"NULL","NULL")
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")

    except(OSError, FileNotFoundError):
        print("error")


    my_image = ImageTk.PhotoImage(Image.open(second_frame.filename).resize((20, 20)))

    listimages.append(my_image)

    Label(second_frame, image=listimages[counter - 1]).pack()

    des = 'Resources\ew' + str(counter) + ".jpg"
    shutil.copy(second_frame.filename, des)
    # os.rename('Resources\ew'+str(counter)+".jpg",'Resources\ew'+str(counter)+".jpg")

    temp_img = face_recognition.load_image_file(des)
    temp_img = cv2.cvtColor(temp_img, cv2.COLOR_BGR2RGB)

    nameEnt = name

    all_face_encodings[nameEnt] = face_recognition.face_encodings(temp_img, model="cnn")[0]
    # print(all_face_encodings[nameEnt])
    face_names = list(all_face_encodings.keys())
    face_encodings = np.array(list(all_face_encodings.values()))


    templist.update(all_face_encodings)
    print(templist)

    with open('dataset_faces.dat', 'wb') as f:
        pickle.dump(templist, f)


#######################################   scroll bar    ##########################################################
main_frame = Frame(root2)
main_frame.pack(fill=BOTH, expand=1)

my_canvas = Canvas(main_frame)
my_canvas.config(bg='Black')
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

second_frame = Frame(my_canvas)
second_frame.config(bg='Black')

Label(second_frame, text="Manage Student Record", bg="black", fg="#2CFF34", font=("Calibri", 15, 'bold')).pack()
my_canvas.create_window((70, 20), window=second_frame, anchor="nw")
#end of scroll bar
#use second frame to insert buttons and stuff


############################################       button functions    ###########################################################

def entername():
    nameEntr = name.get()
    if nameEntr == "":
        Label(second_frame, text="Name not entered", bg="Red", font=("Calibri", 15, 'bold')).pack()


    else:
        list_encoded_names.append(nameEntr)#name list here
        uname = Label(second_frame, text= nameEntr + ' Added', fg='green', bg='Black', font=("Calibri", 12, 'bold')).pack()
        do_encodings(nameEntr)


def delete_all():
    os.remove("dataset_faces.dat")
    templist = {}
    with open('dataset_faces.dat','wb') as f:
        pickle.dump(templist, f)
    with open('dataset_faces.dat', 'rb') as f:
        templist = pickle.load(f)
    print(templist)

    uname = Label(second_frame, text='All Faces are Deleted', fg='red', bg='Black', font=("Calibri", 12, 'bold')).pack()


def delete_one():
    d={}

    nameToDelete = name.get()

    f1=open("dataset_faces.dat","rb")
    d=pickle.load(f1)
    if (nameToDelete not in d.keys()):
        Label(second_frame, text='NAME NOT FOUND', fg='red', bg='Black', font=("Calibri", 12, 'bold')).pack()
    else:
        del d[nameToDelete]
        with open('dataset_faces.dat', 'wb') as f:
            pickle.dump(d, f)
        print(d)
        uname = Label(second_frame, text=nameToDelete +' Deleted', fg='red', bg='Black', font=("Calibri", 12, 'bold')).pack()


#############################################     second frame window   ###################################################

#main part starts here for the window

name = tk.StringVar()

Label(second_frame, bg="Black").pack()
nameEntered = ttk.Entry(second_frame, width=30, textvariable=name)
nameEntered.pack()

Label(second_frame, bg="Black").pack()
RE = Image.open("RE.png")
RE1 = RE.resize((185, 45), Image.ANTIALIAS)
RE2 = ImageTk.PhotoImage(RE1)
registerBtn = tk.Button(second_frame, image=RE2, bg='Black', command=entername, activebackground="black",
                        borderwidth=0).pack()
nameEnt = nameEntered.get()

Label(second_frame, bg="Black", font=("Verdana", 1, 'bold')).pack()
DR = Image.open("DR.png")
DR1 = DR.resize((185, 45), Image.ANTIALIAS)
DR2 = ImageTk.PhotoImage(DR1)
deleteOneBtn = tk.Button(second_frame, image=DR2, bg='Black', command=delete_one, activebackground="black",
                         borderwidth=0).pack()

Label(second_frame, bg="Black", font=("Verdana", 1, 'bold')).pack()
DAD = Image.open("DAD.png")
DAD1 = DAD.resize((185, 45), Image.ANTIALIAS)
DAD2 = ImageTk.PhotoImage(DAD1)
deleteAllBtn = tk.Button(second_frame, image=DAD2, bg='Black', command=delete_all, activebackground="black",
                         borderwidth=0).pack()

Label(second_frame, bg="Black", font=("Verdana", 1, 'bold')).pack()
VD = Image.open("VD.png")
VD1 = VD.resize((185, 45), Image.ANTIALIAS)
VD2 = ImageTk.PhotoImage(VD1)
viewDB = tk.Button(second_frame, image=VD2, bg='Black', command=lambda: [close_windows(), dbview()],
                   activebackground="black", borderwidth=0).pack()

Label(second_frame, text="", bg="Black", height=4).pack()
icon = Image.open("back-button.ico")
icon1 = icon.resize((40, 40), Image.ANTIALIAS)
icon2 = ImageTk.PhotoImage(icon1)
Button(second_frame, image=icon2, bg="black", command=lambda: [close_windows(), dashboardopen()],
       activebackground="black", borderwidth=0).pack(side=LEFT)


def dbview():
    os.system('python viewdatabase.py')

firstlist = {}

templist = {}
filename='dataset_faces.dat'

if os.path.exists(filename):
    with open('dataset_faces.dat', 'rb') as f:
        firstlist = pickle.load(f)
else:
    print("filenot found")
    with open('dataset_faces.dat', 'wb') as f:
        pickle.dump(templist, f)

templist = firstlist
listimages=[]


def close_windows():
    root2.destroy()


def dashboardopen():
    os.system('python dashboard.py')


root2.mainloop()
