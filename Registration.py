from distutils.sysconfig import get_makefile_filename
from tkinter import *
import os

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global Gmail
    global username_entry
    global password_entry
    global Gmail_entry
    username = StringVar()
    password = StringVar()
    Gmail = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="white").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    Gmail_lable = Label(register_screen, text="Gmail * ")
    Gmail_lable.pack()
    Gmail_entry = Entry(register_screen, textvariable=Gmail)
    Gmail_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="white", command = register_user).pack()

def register_user():
 
    username_info = username.get()
    password_info = password.get()
    Gmail_info = Gmail.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    Gmail_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Successfully Registered", fg="green", font=("calibri", 11)).pack()