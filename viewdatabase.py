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


rootview = Tk()
rootview.title("View Database")
rootview.geometry("400x650")
rootview.config(bg="SkyBlue1")
p1 = PhotoImage(file='appicon.png')
rootview.iconphoto(False, p1)

bgi = Image.open("Capture3.jpg")
bgi.image = bgi
bgi1 = bgi.resize((400, 650), Image.ANTIALIAS)
bgi2 = ImageTk.PhotoImage(bgi1)
canvas1 = Canvas(rootview, width=400, height=650)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=bgi2, anchor="nw")
lable1 = Label(canvas1, bg="Black", font=("Verdana", 2, 'bold'))
lable1.pack(pady=10)

count = 0

tempdatabase = {}

f1 = open("dataset_faces.dat", "rb")
tempdatabase = pickle.load(f1)


print(tempdatabase.keys())

listbox = Listbox(canvas1, width=35, height=30, highlightbackground="grey50")
listbox.pack()


for name in tempdatabase.keys():
    print(name)
    listbox.insert(count, name)
    count = count + 1

icon = Image.open("back-button.ico")
icon.image = icon
icon1 = icon.resize((40, 40), Image.ANTIALIAS)
icon2 = ImageTk.PhotoImage(icon1)
Button(canvas1, text="", image=icon2, bg="black", command=lambda: [close_windows(), openregister()],
       activebackground="black", borderwidth=0).pack(side=LEFT, padx=10)


def close_windows():
    rootview.destroy()


def openregister():
    os.system('Python register.py')


rootview.mainloop()