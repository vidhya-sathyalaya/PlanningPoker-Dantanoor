from tkinter import *
from tkinter import messagebox
import atexit

def closewindow():
     result = messagebox.askquestion("Exit", "Are You Sure You Want to Exit?")
     if result == "yes":
        main_screen.destroy()
     else:
        return None

atexit.register(closewindow)  
# Creating the tkinter window

main_screen = Tk()
main_screen.geometry("500x400")
main_screen.title("Planning Poker")
Label(text="Delta Poker", bg="white", width="300", height="2", font=("Calibri", 13)).pack()
Label(text="").pack()

# Button for closing

exit_button = Button(main_screen, text="Exit", command=main_screen.destroy)
exit_button.pack(pady=20)
  
main_screen.mainloop()
