import tkinter as tk
from tkinter import * 
from tkinter import messagebox

def start_new_game():  
    messagebox.showinfo('Message', 'New Game has been initiated!')

main_screen = Tk()
main_screen.geometry("500x400")
main_screen.title("Planning Poker")
Label(text="Delta Poker", bg="white", width="300", height="2", font=("Calibri", 13)).pack()
Label(text="").pack()
Button(text = 'New Game',height="2", width="30", command = start_new_game).pack() 
 
main_screen.mainloop()
