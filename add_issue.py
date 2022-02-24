from tkinter import *

main_screen = Tk()
main_screen.title("ADD ISSUE")

def addIssue():
    issue = Entry(main_screen)
    issue.pack()

    
    def showIssue():
    
        show_issue = Label(main_screen, text=issue.get()).pack()

    submit_issue = Button(main_screen,text='Submit Issue',command=showIssue).pack()
    
    return issue 




Issue_button = Button(main_screen, text = "Add Issue",command=addIssue).pack()
main_screen.mainloop()
