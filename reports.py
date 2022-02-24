# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="",
#   database="faceapp"
# )
# print(mydb)
# mycursor = mydb.cursor()
#
# mycursor.execute("select DISTINCT dyString,COUNT(name) FROM attendance GROUP BY dyString")
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)
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


root=Tk()
root.geometry("400x500")

root.mainloop()
