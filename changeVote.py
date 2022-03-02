from tkinter import *
from tkinter import messagebox
import tkinter
  
# Top level window
main_screen = tkinter.Tk()
main_screen.geometry("500x300")
main_screen.title("Planning Poker")

# Function for getting Input
# from textbox and printing it 
# at label widget
  
def changeVote():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Provided Input: "+inp)
  
# TextBox Creation
inputtxt = tkinter.Text(main_screen,
                   height = 2,
                   width = 20)
  
inputtxt.pack()
  
# Button Creation
changeVoteButton = tkinter.Button(main_screen,
                        text = "Change Vote", 
                        command = changeVote)
changeVoteButton.pack()
  
# Label Creation
lbl = tkinter.Label(main_screen, text = "")
lbl.pack()
main_screen.mainloop()
