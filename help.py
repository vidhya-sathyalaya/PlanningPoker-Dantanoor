import tkinter as tk
from tkinter import * 
import turtle
import json

root=tk.Tk()
root.geometry("500x300")
root.configure(bg='white')

root.title("Planning Poker")
def help_screen():

        help_window = Tk()
        help_window.title("Help Screen")

        new_game_lbl = Label(help_window, text = "new_game - This is used to start a new game")
        new_game_lbl.grid(column = 10, row = 10)

        new_game_lbl = Label(help_window, text = "Login - Login if you are previously register to the game")
        new_game_lbl.grid(column = 10, row = 20)

        new_game_lbl = Label(help_window, text = "Registered - Register if you are new for this game")
        new_game_lbl.grid(column = 10, row = 30)

        EOF_lbl = Label(help_window, text = "Exit - Exit from the game")
        EOF_lbl.grid(column = 10, row = 40)
        
        add_player_lbl = Label(help_window, text = "add_player - Click add player to add new player to the game")
        add_player_lbl.grid(column = 10, row = 50)
        
        current_issue_lbl = Label(help_window, text = "Vote_issue - To vote an issue or to raise an issue")
        current_issue_lbl.grid(column = 10, row = 60)

        next_issue_lbl = Label(help_window, text = "next_issue - This is used to go to the next issue")
        next_issue_lbl.grid(column = 10, row = 70)

        previous_issue_lbl = Label(help_window, text = "previous_issue - This is used to go to the previous issue")
        previous_issue_lbl.grid(column = 10, row = 80)

        remove_player_lbl = Label(help_window, text = "remove_player - This is used to remove a player")
        remove_player_lbl.grid(column = 10, row = 90)

        reset_votes_lbl = Label(help_window, text = "reset_votes - This is used to reset the votes of an issue")
        reset_votes_lbl.grid(column = 10, row = 100)

        show_report_lbl = Label(help_window, text = "show_report - This is used to show the voting report")
        show_report_lbl.grid(column = 10, row = 110)
        
        user_count_lbl = Label(help_window, text = "user_count - This is used to show the number of players in the game")
        user_count_lbl.grid(column = 10, row = 120)

        vote_issue_lbl = Label(help_window, text = "vote_issue - This is used to cast a vote to an issue")
        vote_issue_lbl.grid(column = 10, row = 130)

        voting_system_lbl = Label(help_window, text = "voting_system - This is used to view the voting system of the game")
        voting_system_lbl.grid(column = 10, row = 140)
        help_window.mainloop()
btn2=tk.Button(root,text='HELP', height="1",width="20", bd=8, font=('arial', 15, 'bold'), command=help_screen)
btn2.place(x = 100, y = 100)
mainloop()