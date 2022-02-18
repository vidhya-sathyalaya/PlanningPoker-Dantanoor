from distutils.sysconfig import get_makefile_filename
from tkinter import *
import os

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("500x400")
    main_screen.title("Planning Poker")
    Label(text="Delta Poker", bg="white", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    img=PhotoImage(file='logo2.png')
    Label(main_screen,image=img). pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()
 
 
main_account_screen()