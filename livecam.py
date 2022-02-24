import pickle
import mysql.connector
import face_recognition
import cv2
import numpy as np

import numpy as np

from PIL import ImageTk, Image
from datetime import datetime

from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import shutil, os
import os
import threading

global cam_used
cam_used = 1
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
            # f.writelines(f'\n{name},{dtString}')
            i = 0
            # listbox.insert(i, name)
            i = i + 1


video_capture = cv2.VideoCapture(cam_used)

with open('dataset_faces.dat', 'rb') as f:
    all_face_encodings = pickle.load(f)

    known_face_names = list(all_face_encodings.keys())

    known_face_encoding = np.array(list(all_face_encodings.values()))

    print(len(known_face_encoding))

    print(len(known_face_names))

# Initialize some variables


face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
            name = "Unknown"

            face_distances = face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            markAttendance(name)
            face_names.append(name)

    process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()