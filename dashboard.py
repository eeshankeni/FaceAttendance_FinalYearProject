from tkinter import *
import os
import threading
from PIL import Image
from PIL import ImageTk

LARGEFONT = ("Verdana", 13)

start_page = Tk()


def openfaceapp():
    os.system('python faceapp.py')


def close_windows():
    start_page.destroy()


def new_register_thread():
    os.system('python register.py')


def New_Register():

    t1 = threading.Thread(target=new_register_thread)
    t1.start()


def markAttendance_thread():
    os.system('python AttendanceMarker.py')


def MarkAttendance():
    t2 = threading.Thread(target=markAttendance_thread)
    t2.start()


def viewattendance_thread():
    os.system('python ViewAttendance.py')


def ViewAttendance():
    t2 = threading.Thread(target=viewattendance_thread)
    t2.start()
# Deleting popups

def viewreports():
    os.system('python graphs.py')

start_page.title("Home Page")
start_page.geometry("500x360")
p1 = PhotoImage(file='appicon.png')
start_page.iconphoto(False, p1)

# Background Image
bgi = Image.open("Capture1.png")
bgi.image = bgi
bgi1 = bgi.resize((500, 360), Image.ANTIALIAS)
bgi2 = ImageTk.PhotoImage(bgi1)
canvas1 = Canvas(start_page, width=500, height=360)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bgi2, anchor="nw")

MS = Image.open("MS.png")
MS.image = MS
MS1 = MS.resize((185, 45), Image.ANTIALIAS)
MS2 = ImageTk.PhotoImage(MS1)
button1 = Button(start_page, image=MS2, bg="black", command=lambda: [close_windows(), New_Register()], borderwidth=0,
                 activebackground="black")

MA = Image.open("MA.png")
MA.image = MA
MA1 = MA.resize((185, 45), Image.ANTIALIAS)
MA2 = ImageTk.PhotoImage(MA1)
button2 = Button(start_page, image=MA2, bg="black", command=lambda: [close_windows(), MarkAttendance()], borderwidth=0,
                 activebackground="black")

VA = Image.open("VA.png")
VA.image = VA
VA1 = VA.resize((185, 45), Image.ANTIALIAS)
VA2 = ImageTk.PhotoImage(VA1)
button3 = Button(start_page, image=VA2, bg='black', borderwidth=0, command=lambda: [close_windows(), viewreports()],
                 activebackground='black')

LO = Image.open("LO.png")
LO.image = LO
LO1 = LO.resize((185, 45), Image.ANTIALIAS)
LO2 = ImageTk.PhotoImage(LO1)
button4 = Button(start_page, image=LO2, bg="black", command=close_windows, activebackground="black", borderwidth=0)

button1_canvas = canvas1.create_window(155, 50, anchor="nw", window=button1)
button2_canvas = canvas1.create_window(155, 120, anchor="nw", window=button2)
button3_canvas = canvas1.create_window(155, 190, anchor="nw", window=button3)
button4_canvas = canvas1.create_window(155, 260, anchor="nw", window=button4)

start_page.mainloop()