# Person reports
import mysql.connector
from tkinter import *
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

root.mainloop()