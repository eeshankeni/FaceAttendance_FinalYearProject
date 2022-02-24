from tkinter import *
import os
import threading
from PIL import Image
from PIL import ImageTk

LARGEFONT = ("Verdana", 13)

start_page = Tk()

def g_markAttendance_thread():
    os.system('')


def g_MarkAttendance():
    t2 = threading.Thread(target=g_markAttendance_thread())
    t2.start()
    os.system('python graphs.py')



def i_markAttendance_thread():
    os.system('python individual.py')


def i_MarkAttendance():
    t2 = threading.Thread(target=i_markAttendance_thread)
    t2.start()


def backbtn_thread():
    os.system('python dashboard.py')


def Backbutton():
    t2 = threading.Thread(target=backbtn_thread)
    t2.start()


def close_windows():
    start_page.destroy()


start_page.title("View Attendance")
start_page.geometry("300x250")
p1 = PhotoImage(file='appicon.png')
start_page.iconphoto(False, p1)

# Background Image
bgi = Image.open("Capture1.png")
bgi.image = bgi
bgi1 = bgi.resize((300, 250), Image.ANTIALIAS)
bgi2 = ImageTk.PhotoImage(bgi1)
canvas1 = Canvas(start_page, width=300, height=250)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bgi2, anchor="nw")

IA = Image.open("IA.png")
IA.image = IA
IA1 = IA.resize((185, 45), Image.ANTIALIAS)
IA2 = ImageTk.PhotoImage(IA1)
button1 = Button(start_page, image=IA2, bg="black", borderwidth=0, activebackground="black",
                 command=lambda: [close_windows(), i_MarkAttendance()])

GA = Image.open("GA.png")
GA.image = GA
GA1 = GA.resize((185, 45), Image.ANTIALIAS)
GA2 = ImageTk.PhotoImage(GA1)
button2 = Button(start_page, image=GA2, bg="black", borderwidth=0, activebackground="black",
                 command=lambda: [close_windows(), g_MarkAttendance()])

icon = Image.open("back-button.ico")
icon1 = icon.resize((40, 40), Image.ANTIALIAS)
icon2 = ImageTk.PhotoImage(icon1)
button3 = Button(start_page, image=icon2, bg="black", command=lambda: [close_windows(), Backbutton()],
                 activebackground="black", borderwidth=0)

canvas1.create_text(150, 30, text="Chose Operation", fill='white', font=("Verdana", 13, 'bold'))
button1_canvas = canvas1.create_window(60, 60, anchor="nw", window=button1)
button2_canvas = canvas1.create_window(60, 130, anchor="nw", window=button2)
button3_canvas = canvas1.create_window(10, 190, anchor="nw", window=button3)

start_page.mainloop()