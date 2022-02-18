import tkinter as tk
from tkinter import * 
from tkinter import messagebox
import turtle


root=tk.Tk()
root.title("Planning poker App")  
root.geometry("500x400")
root.configure(bg='white')
addplayer=tk.StringVar() 
players = []
def showNames():
    for i in range(len(players)):
        txt = tk.Text(root,width=15,height=2)
        txt.grid(row=4,column=i)
        txt.insert(tk.END,players[i])
def click():    
   tk.messagebox.showinfo("Message",  "You have registered as a player"+addplayer.get())
   add_player_name=addplayer.get()
   players.append(add_player_name)
   print(players)
   showNames()



name_label = tk.Label(root, text = 'Player Name', fg="white", bg="orange", font=('roman',15, 'bold'))
name_label.grid(row=1,column=1)

name_entry = tk.Entry(root,textvariable = addplayer, font=('roman',15,'normal'))
name_entry.grid(row=1,column=2)

sub_btn=tk.Button(root,text = 'ADD',height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="green",
bg="white",command = click)
sub_btn.grid(row=3,column=1)

exit_btn1=tk.Button(root,text='Exit', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="red",command=quit)
exit_btn1.grid(row=3,column=2)

root.mainloop()