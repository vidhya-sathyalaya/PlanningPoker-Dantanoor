from distutils.sysconfig import get_makefile_filename
import json
import time
from tkinter import *
import tkinter
from tkinter import messagebox
from webbrowser import get
from Registration import *
from fastapi import status

import os

from gui_client_util import GUI_Helper

def open_another_file(filename):
    os.system('python ' + filename)

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

def parse_report(report):
        ret_str = ""
        for vote_value, vote_details in report.items():
            json_details = json.dumps(vote_details['voters'])
            vote_count = vote_details['vote_count']
            ret_str += str(vote_count) + "voted for " + str(vote_value) + "story points.\n" + json_details+ "\n"
        return ret_str

def get_report():
    current_status = 'pending'
    retry_count = 0
    while current_status == 'pending' and retry_count < util.max_retries:
            response = util.send_request(method='get',
                                         route='/issue/show_results')
            
            if response.status_code == status.HTTP_200_OK:
                response_message = json.loads(response.text)['result_message']
                current_status = response_message['status']
                ret_str = "Pending votes"
                if current_status == 'done':
                   ret_str = parse_report(response_message['report'])
                return ret_str
            else:
                current_status = 'error'
                return "Failure fetching the Report"
            

def show_report():
    tkinter.messagebox.showinfo(title="The Report", message=get_report())

def closewindow():
    
    result = tkinter.messagebox.askquestion("Exit", "Are You Sure You Want to Exit?")
    if result == "yes":
        main_screen.destroy()
    
    else:
        return None


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("600x650")
    main_screen.title("Planning Poker")
    Label(text="Delta Poker", bg="white", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    img=PhotoImage(file='logo2.png')
    Label(main_screen,image=img). pack()
    Label(text="").pack()
    Button(text="Add Issue", height="2", width="30", command=lambda: open_another_file('add_issue.py')).pack()
    Label(text="").pack()
    Button(text="Show Current Issue", height="2", width="30", command=showCurrIssue).pack()
    Label(text="").pack()
    Button(text="Show Report", height="2", width="30", command=show_report).pack()
    Label(text="").pack()
    Button(text="Justify vote", height="2", width="30", command=lambda: open_another_file('player_justification.py')).pack()
    Label(text="").pack()
    Button(text="Showdown", height="2", width="30", command=lambda: open_another_file('showdown.py')).pack()
    Label(text="").pack()
    Button(main_screen, text="Exit",height="2", width="30",  command=closewindow).pack()
    
 
    main_screen.mainloop()

main_account_screen()
