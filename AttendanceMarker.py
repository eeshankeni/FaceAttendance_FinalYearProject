#### AttendenceMarker.py ####
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
import shutil, os
import os
import threading
from tkinter.ttk import Progressbar
import sqlite3
import mysql.connector

filename = "attendance.csv"
f = open(filename, "w+")
f.close()

root = Tk()
root.title("Take Attendance")
root.geometry("500x790")

p1 = PhotoImage(file='appicon.png')
root.iconphoto(False, p1)

bgi = Image.open("Capture1.png")
bgi.image = bgi
bgi1 = bgi.resize((500, 200), Image.ANTIALIAS)
bgi2 = ImageTk.PhotoImage(bgi1)
canvas = Canvas(root, width=500, height=200)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bgi2, anchor="nw")

progress = ttk.Progressbar(canvas, orient=HORIZONTAL, length=400, mode='indeterminate')
progress.grid(column=0, row=0, columnspan=8, padx=50, pady=30)


def bar():
    value = 0
    import time
    for x in range(1, 100):
        progress['value'] = x
        root.update_idletasks()
        time.sleep(0.05)

    bar()


###############################################  live attendance  ############################################
def livecam_thread():
    os.system('python livecam.py')


def live():
    t3 = threading.Thread(target=livecam_thread)
    t3.start()


def fillList():
    with open("attendance.csv", 'r+') as f:
        myDatalist = f.readlines()
        print(myDatalist)
        nameList = []
        print(nameList)
        for line in myDatalist:
            entry = line.split(',')
            nameList.append(entry[0])
            i = 0
            print(entry[i])
            if "Unknown" not in entry[0]:
                listbox.insert(i, entry[0])
                i = i + 1

        print(nameList)


###############################################  group attendance  ############################################
def openfiles():
    global my_image
    canvas1.filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(
        ("Image files", ".png",), ("Image files", ".jpg",), ("all files", ".")))

    my_image = ImageTk.PhotoImage(Image.open(canvas1.filename).resize((300, 180)))
    canvas1.create_image(255, 505, image=my_image)

    des = 'Resources\group.jpg'
    shutil.copy(canvas1.filename, des)
    os.rename('Resources\overview-Barack-Obama.jpg', 'Resources\group.jpg')


def markAttendance(name):
    with open("attendance.csv", 'r+') as f:
        myDatalist = f.readlines()
        nameList = []
        for line in myDatalist:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime("%H:%M:%S")
            dyString = now.strftime("%d-%m-%y")
            f.writelines(f'\n{name},{dtString},{dyString}')

            # conn = sqlite3.connect("faceapp.db")
            #
            # c = conn.cursor()
            #
            # # c.executemany("INSERT INTO attendance VALUES (?,?,?)",name,dtString,timeString)
            # # query = f"INSERT INTO attendance VALUES name,dtString,timeString"
            # # c.execute(query)
            # c.execute("INSERT INTO table VALUES (%s, %s, %s)", (name, dtString, timeString))
            #
            # print(c.fetchall())
            # conn.commit()
            # conn.close()

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
            val = (name, dtString, dyString)
            mycursor.execute(sql, val)

            mydb.commit()

            print(mycursor.rowcount, "record inserted.")

            i = 0
            listbox.insert(i, name)
            i = i + 1

def pressed():

    tester = 1
    # LOADING FACE DATA
    with open('dataset_faces.dat', 'rb') as f:
        all_face_encodings = pickle.load(f)

    # ADDING ENCODING TO LIST

    known_face_names = list(all_face_encodings.keys())

    dist = []

    known_face_encoding = np.array(list(all_face_encodings.values()))

    print(len(known_face_encoding))

    print(len(known_face_names))

    # LOADING TEST IMAGE
    test_image = face_recognition.load_image_file('Resources\group.jpg')

    print("loaded group")

    # detecting faces in test
    face_locations = face_recognition.face_locations(test_image)  # , number_of_times_to_upsample=1, model="cnn")
    face_encodings = face_recognition.face_encodings(test_image, face_locations)  # , num_jitters=2000)

    print("encoded")

    # converting to PIL
    pill_image = Image.fromarray(test_image)

    # imagedraw

    print("draw")
    draw = ImageDraw.Draw(pill_image)
    count = 0
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
        print(matches)
        dist = face_recognition.face_distance(known_face_encoding, face_encoding)
        print(dist)

        name = "UNKNOWN PERSON"

        best_match_index = np.argmin(dist)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            print(count)
            count = count + 1
            markAttendance(name)

        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 0))
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height), (right, bottom + 5)), fill=(0, 0, 0), outline=(0, 0, 0))
        draw.text((left + 6, bottom - text_height), name, fontsize=50, fill=(255, 255, 255, 255))

    del draw

    pill_image.show()
    eigen = 1
    cv2.waitKey(0)


def func1(evt=None):
    eigen = 0
    threading.Thread(target=bar).start()

    pressed()


## canvas ##
IGP = Image.open("IGP.png")
IGP.image = IGP
IGP1 = IGP.resize((185, 40), Image.ANTIALIAS)
IGP2 = ImageTk.PhotoImage(IGP1)
my_btn1 = Button(canvas, image=IGP2, bg='black', borderwidth=0, command=openfiles, activebackground="black")
button1_canvas = canvas.create_window(170, 60, anchor="nw", window=my_btn1)

MGA = Image.open("MGA.png")
MGA.image = MGA
MGA1 = MGA.resize((185, 40), Image.ANTIALIAS)
MGA2 = ImageTk.PhotoImage(MGA1)
my_btn2 = Button(canvas, image=MGA2, command=lambda: threading.Thread(target=func1).start(), borderwidth=0,
                 activebackground="black", bg="black")
button2_canvas = canvas.create_window(170, 120, anchor="nw", window=my_btn2)


## Live Attendance & canvas1 ##
bg = Image.open("Capture3.jpg")
bg.image = bg
bg1 = bg.resize((500, 790), Image.ANTIALIAS)
bg2 = ImageTk.PhotoImage(bg1)
canvas1 = Canvas(root, width=500, height=500)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bg2, anchor="nw")

LA = Image.open("LA.png")
LA.image = LA
LA1 = LA.resize((185, 40), Image.ANTIALIAS)
LA2 = ImageTk.PhotoImage(LA1)
my_btn3 = Button(canvas1, image=LA2, command=live, bg="black", activebackground="black", borderwidth=0)
button3_canvas = canvas1.create_window(170, 20, anchor="nw", window=my_btn3)

FAL = Image.open("FAL.png")
FAL.image = FAL
FAL1 = FAL.resize((185, 40), Image.ANTIALIAS)
FAL2 = ImageTk.PhotoImage(FAL1)
my_btn4 = Button(canvas1, image=FAL2, command=fillList, activebackground="black", bg="black", borderwidth=0)
button4_canvas = canvas1.create_window(170, 80, anchor="nw", window=my_btn4)

listbox = Listbox(canvas1, width=35, height=15, highlightbackground="grey50")
listbox_canvas = canvas1.create_window(155, 130, anchor="nw", window=listbox)

canvas1.create_text(260, 395, text="PRESS Q TO CLOSE CAMERA", fill="red", font=("Arial", 20, 'bold'))

icon = Image.open("back-button.ico")
icon1 = icon.resize((40, 40), Image.ANTIALIAS)
icon2 = ImageTk.PhotoImage(icon1)
my_btn5 = Button(canvas1, image=icon2, bg="black", command=lambda: [close_windows(), dashboardopen()],
                 activebackground="black", borderwidth=0)
button5_canvas = canvas1.create_window(10, 550, anchor="nw", window=my_btn5)


def close_windows():
    root.destroy()


def dashboardopen():
    os.system('python dashboard.py')


root.mainloop()