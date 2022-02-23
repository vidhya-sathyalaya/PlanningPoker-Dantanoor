import tkinter as tk
from tkinter import * 
from tkinter import messagebox
import turtle


root=tk.Tk()
root.title("Planning poker App-Display players names and their vote for issue")  
root.geometry("500x400")
root.configure(bg='white')
addplayer=tk.StringVar() 
players = ['Player A','Player B','Player C','Player D']
issues = ['Issue A','Issue B','Issue C','Issue D']


player_variable = StringVar(root)
player_variable.set(players[0]) # default value

player_w = OptionMenu(root, player_variable, *players)
player_w.pack()

player_w.place(x=25,y=0)

issue_variable = StringVar(root)
issue_variable.set(issues[0]) # default value

issue_w = OptionMenu(root, issue_variable, *issues)
issue_w.pack()

issue_w.place(x=150,y=0)


player_vote={}


def showNames():
    j=0
    for i in player_vote:
        txt = tk.Text(root,width=200,height=300)
        txt.place(x=25,y=j+50)
        j=j+50
        votes=",".join(player_vote.get(i))
        textfin=i+" : "+votes
        txt.insert(tk.END,textfin)
def click():    
    if(player_variable.get() in player_vote):
       player_vote.get(player_variable.get()).add(issue_variable.get())
    else:
        player_vote[player_variable.get()]={issue_variable.get()}
    print(player_vote)
    showNames()

button = Button(root, text="Vote", command=click)
button.pack()




root.mainloop()