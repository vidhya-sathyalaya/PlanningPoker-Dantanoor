from distutils.sysconfig import get_makefile_filename
import json
from tkinter import *
import tkinter
from tkinter import messagebox
from webbrowser import get
from Registration import *
from fastapi import status

import os

from gui_client_util import GUI_Helper

def login():
    pass
util = GUI_Helper()

def get_current_issue():
    response = util.send_request(method='get',
                                     route='/issue/current')
    if response.status_code == status.HTTP_200_OK:
            response_dict = json.loads(response.text)
            curr_issue_title = response_dict['result_message']['title']
            curr_issue_desc = response_dict['result_message']['description']

            if len(curr_issue_desc) > 0:
                return curr_issue_title+ " - " + curr_issue_desc
            else:
                return curr_issue_title
    else:
            return "Failure fetching current issue"

def showCurrIssue():
    tkinter.messagebox.showinfo(title="Current Issue", message=get_current_issue())

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
    Label(text="").pack()
    Button(text="Show Current Issue", height="2", width="30", command=showCurrIssue).pack()
 
    main_screen.mainloop()

main_account_screen()