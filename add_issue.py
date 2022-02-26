from tkinter import *
import tkinter

main_screen = Tk()
main_screen.title("ADD ISSUE")

def sendIssueToServer():
    pass
def addIssue():
    
    main_screen.geometry("300x100")

    Label(text="Issue Title").grid(row=0, column=0)
    issue_name = Entry(main_screen)
    issue_name.grid(row=0, column=1)
    Label(text="Issue Description").grid(row=1, column=0)
    issue_desc = Entry(main_screen)
    issue_desc.grid(row=1, column=1)
    Label(text="").grid(row=2)

    
    def showIssue():
    
        show_issue = Label(main_screen, text=issue_name.get()).grid(row=4)

    submit_issue = Button(main_screen,text='Submit Issue',command=showIssue).grid(row=3, column=1)
    
    main_screen.mainloop()


addIssue()
