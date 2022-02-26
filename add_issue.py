import json
from tkinter import *
import tkinter
from gui_client_util import GUI_Helper
from fastapi import status

util = GUI_Helper()
issue_window = Tk()
issue_window.title("ADD ISSUE")


def addIssue():
    
    issue_window.geometry("300x150")

    Label(text="Issue Title").grid(row=0, column=0)
    issue_name = Entry(issue_window)
    issue_name.grid(row=0, column=1)
    Label(text="Issue Description").grid(row=1, column=0)
    issue_desc = Entry(issue_window)
    issue_desc.grid(row=1, column=1)
    Label(text="").grid(row=2)

    def sendIssueToServer():
        

        issue_data = {
            'title': issue_name.get(),
            'description': issue_desc.get()
        }
        
        
        response = util.send_request(method='put',
                                     route='/issue/add',
                                     data=issue_data)
                                    
        result_txt = ""
        #print(f"{json.dumps(json.loads(response.text), indent=4)}")

        if response.status_code == status.HTTP_200_OK:
            response_dict = json.loads(response.text)
            result_txt= "Issue added successfully"
            
        else:
            result_txt= "Received " + str(response.status_code) + " from server"
        Label(issue_window, text=result_txt).grid(row=4)
        

    def showIssue():
    
        show_issue = Label(issue_window, text=issue_name.get()).grid(row=4)

    submit_issue = Button(issue_window,text='Submit Issue',command=sendIssueToServer).grid(row=3, column=1)
    
    issue_window.mainloop()


addIssue()
