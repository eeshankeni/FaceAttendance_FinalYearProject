from tkinter import *
import os
import threading
from PIL import Image
from PIL import ImageTk

LARGEFONT = ("Verdana", 13)


##  View pages  ##
def StartPage():
    global start_page
    start_page = Toplevel(main_screen)
    p1 = PhotoImage(file='appicon.png')
    start_page.iconphoto(False, p1)
    start_page.geometry("300x250")
    start_page.title("Account Login")
    bgi = Image.open("Capture1.png")
    bgi.image = bgi
    bgi1 = bgi.resize((300, 250), Image.ANTIALIAS)
    bgi2 = ImageTk.PhotoImage(bgi1)
    canvas2 = Canvas(start_page, width=300, height=250)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=bgi2, anchor="nw")

    # canvas2.create_text(150, 40, text="Select Your Choice", fill='white', font=("Calibri", 15, 'bold'))
    #
    # lgi = Image.open("login.png")
    # lgi.image = lgi
    # lgi1 = lgi.resize((185, 45), Image.ANTIALIAS)
    # lgi2 = ImageTk.PhotoImage(lgi1)
    # btn1 = Button(start_page, image=lgi2, activebackground="black", bg="black", command=login, borderwidth=0)
    # canvas2.create_window(60, 80, anchor="nw", window=btn1)
    #
    # re = Image.open("re_1.png")
    # re.image = re
    # re1 = re.resize((185, 45), Image.ANTIALIAS)
    # re2 = ImageTk.PhotoImage(re1)
    # btn2 = Button(start_page, image=re2, command=register, bg="black", activebackground="black", borderwidth=0)
    # canvas2.create_window(60, 150, anchor="nw", window=btn2)

    start_page.mainloop()


def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    p1 = PhotoImage(file='appicon.png')
    login_screen.iconphoto(False, p1)

    bgi = Image.open("Capture1.png")
    bgi.image = bgi
    bgi1 = bgi.resize((300, 250), Image.ANTIALIAS)
    bgi2 = ImageTk.PhotoImage(bgi1)
    canvas2 = Canvas(login_screen, width=300, height=250)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=bgi2, anchor="nw")

    canvas2.create_text(150, 40, text="Please enter details below to login", fill='white', font=("Calibri", 13, 'bold'))

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    canvas2.create_text(155, 80, text="Username *", fill='white', font=("Verdana", 8, 'bold'))
    username_login_entry = Entry(canvas2, textvariable=username_verify)
    username_login_entry.place(x=90, y=95)

    canvas2.create_text(155, 130, text="Password *", fill='white', font=("Verdana", 8, 'bold'))
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.place(x=90, y=145)

    lgi = Image.open("login.png")
    lgi.image = lgi
    lgi1 = lgi.resize((150, 40), Image.ANTIALIAS)
    lgi2 = ImageTk.PhotoImage(lgi1)
    li_btn = Button(login_screen, image=lgi2, bg="black", borderwidth=0, activebackground="black", command=login_verify)
    canvas2.create_window(75, 180, anchor="nw", window=li_btn)

    login_screen.mainloop()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("300x250")
    p1 = PhotoImage(file='appicon.png')
    login_success_screen.iconphoto(False, p1)

    bgi = Image.open("Capture1.png")
    bgi.image = bgi
    bgi1 = bgi.resize((300, 250), Image.ANTIALIAS)
    bgi2 = ImageTk.PhotoImage(bgi1)
    canvas2 = Canvas(login_success_screen, width=300, height=250)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=bgi2, anchor="nw")

    canvas2.create_text(155, 90, text="Login Success", fill='green', font=("Calibri", 15, 'bold'))

    btn = Button(login_success_screen, text="OK", command=lambda: [close_windows(), dashboardopens()], fg="white",
                 activebackground="cyan", bg="#000066")
    canvas2.create_window(140, 130, anchor="nw", window=btn)

    login_success_screen.mainloop()


def dashboardopens():
    os.system('python dashboard.py')


# Designing popup for login invalid password
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Password Failure")
    password_not_recog_screen.geometry("300x250")
    p1 = PhotoImage(file='appicon.png')
    password_not_recog_screen.iconphoto(False, p1)

    bgi = Image.open("Capture1.png")
    bgi.image = bgi
    bgi1 = bgi.resize((300, 250), Image.ANTIALIAS)
    bgi2 = ImageTk.PhotoImage(bgi1)
    canvas2 = Canvas(password_not_recog_screen, width=300, height=250)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=bgi2, anchor="nw")

    canvas2.create_text(155, 50, text="Invalid Password", fill='red', font=("Calibri", 15, 'bold'))
    canvas2.create_text(155, 80, text="Please Enter Password Again", fill='red', font=("Calibri", 15, 'bold'))

    btn = Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised, fg="white",
                 activebackground="cyan", bg="#000066")
    canvas2.create_window(140, 120, anchor="nw", window=btn)

    password_not_recog_screen.mainloop()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


# Designing popup for user not found
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("User ID Failure")
    user_not_found_screen.geometry("300x250")

    p1 = PhotoImage(file='appicon.png')
    user_not_found_screen.iconphoto(False, p1)

    bgi = Image.open("Capture1.png")
    bgi.image = bgi
    bgi1 = bgi.resize((300, 250), Image.ANTIALIAS)
    bgi2 = ImageTk.PhotoImage(bgi1)
    canvas2 = Canvas(user_not_found_screen, width=300, height=250)
    canvas2.pack(fill="both", expand=True)
    canvas2.create_image(0, 0, image=bgi2, anchor="nw")

    canvas2.create_text(155, 50, text="User Not Found", fill='red', font=("Calibri", 15, 'bold'))
    canvas2.create_text(155, 80, text="Please Enter Correct Details", fill='red', font=("Calibri", 15, 'bold'))

    btn = Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen, fg="white",
                 activebackground="cyan", bg="#000066")
    canvas2.create_window(140, 120, anchor="nw", window=btn)

    user_not_found_screen.mainloop()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
    p1 = PhotoImage(file='appicon.png')
    register_screen.iconphoto(False, p1)

    bgi = Image.open("Capture1.png")
    bgi.image = bgi
    bgi1 = bgi.resize((300, 250), Image.ANTIALIAS)
    bgi2 = ImageTk.PhotoImage(bgi1)
    canvas3 = Canvas(register_screen, width=300, height=250)
    canvas3.pack(fill="both", expand=True)
    canvas3.create_image(0, 0, image=bgi2, anchor="nw")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    canvas3.create_text(150, 30, text="Please enter details below", fill='white', font=("Calibri", 13, 'bold'))

    canvas3.create_text(155, 60, text="Username *", fill='white', font=("Verdana", 8, 'bold'))

    username_entry = Entry(canvas3, textvariable=username)
    username_entry.place(x=90, y=75)

    canvas3.create_text(155, 110, text="Password *", fill='white', font=("Verdana", 8, 'bold'))

    password_entry = Entry(canvas3, textvariable=password, show='*')
    password_entry.place(x=90, y=125)

    re = Image.open("re_1.png")
    re.image = re
    re1 = re.resize((150, 40), Image.ANTIALIAS)
    re2 = ImageTk.PhotoImage(re1)
    btn2 = Button(register_screen, image=re2, command=register_user, bg="black", activebackground="black", borderwidth=0)
    canvas3.create_window(75, 160, anchor="nw", window=btn2)

    register_screen.mainloop()


def register_user():
    global reg_user
    reg_user = Toplevel(register_screen)
    reg_user.title("User Registered Success")
    reg_user.geometry("300x150")
    p1 = PhotoImage(file='appicon.png')
    reg_user.iconphoto(False, p1)

    bgi = Image.open("Capture1.png")
    bgi.image = bgi
    bgi1 = bgi.resize((300, 150), Image.ANTIALIAS)
    bgi2 = ImageTk.PhotoImage(bgi1)
    canvas4 = Canvas(reg_user, width=300, height=150)
    canvas4.pack(fill="both", expand=True)
    canvas4.create_image(0, 0, image=bgi2, anchor="nw")

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    canvas4.create_text(150, 30, text="User Registered Successfully", fill='green', font=("Calibri", 13, 'bold'))

    my_btn = Button(reg_user, text="OK", bg="#000066", fg="white", command=lambda: [close_windows1(), main_account_screen],
                    activebackground="cyan")
    canvas4.create_window(140, 80, anchor="nw", window=my_btn)
    reg_user.mainloop()


# eliminate popups
def close_windows():
    main_screen.destroy()


def close_windows1():
    reg_user.destroy()
    register_screen.destroy()
    # start_page.destroy()


# Designing Main(first) window
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.config(bg='SkyBlue1')
    main_screen.title("Attendance Marker")
    p1 = PhotoImage(file='appicon.png')
    main_screen.iconphoto(False, p1)

    bgi = Image.open("Capture1.png")
    bgi.image = bgi
    bgi1 = bgi.resize((300, 250), Image.ANTIALIAS)
    bgi2 = ImageTk.PhotoImage(bgi1)
    canvas1 = Canvas(main_screen, width=300, height=250)
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0, 0, image=bgi2, anchor="nw")

    canvas1.create_text(150, 40, text="Select Your Choice", fill='white', font=("Calibri", 15, 'bold'))

    lgi = Image.open("login.png")
    lgi.image = lgi
    lgi1 = lgi.resize((185, 45), Image.ANTIALIAS)
    lgi2 = ImageTk.PhotoImage(lgi1)
    btn1 = Button(main_screen, image=lgi2, activebackground="black", bg="black", command=login, borderwidth=0)
    canvas1.create_window(60, 80, anchor="nw", window=btn1)

    re = Image.open("re_1.png")
    re.image = re
    re1 = re.resize((185, 45), Image.ANTIALIAS)
    re2 = ImageTk.PhotoImage(re1)
    btn2 = Button(main_screen, image=re2, command=register, bg="black", activebackground="black", borderwidth=0)
    canvas1.create_window(60, 150, anchor="nw", window=btn2)




    main_screen.mainloop()


main_account_screen()
