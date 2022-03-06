from tkinter import *
from tkinter import messagebox

main = Tk()
main.title("Player Judgement")

# initialize lists
player_list = []
description_list = []

# heading label 

heading_label = Label(main, text="Player Justification for the vote case", relief = SUNKEN, bd = 1)
heading_label.grid(row=0, column = 0, sticky = W+E, padx=25, pady=25, columnspan = 3)


# functions for buttons

def submit():

    player_list.append(player_name.get())
    player_name.delete(0, END)
    

    description_list.append(player_description.get())
    player_description.delete(0, END)

def open(value):
    messagebox.showinfo("Player Description", description_list[value])

def display():
    d=Toplevel()
    d.title("Showdown")
    judgement= IntVar()
    judgement.set(0)
    for i in player_list:
        Radiobutton(d, text = i, variable=judgement, value = player_list.index(i)).pack(anchor=W)
    show_description=Button(d, text="Show Description", command = lambda: open(judgement.get())).pack(pady=15)

    
    


# player name and entry box

    player_label = Label(main, text="Enter player name: ")
    player_label.grid(row=1, column = 0, columnspan=1)
    player_name = Entry(main)
    player_name.grid(row = 1, column = 1, columnspan = 2, pady = 5)
    player = player_name.get()

# player judgement and entry box

    description_label = Label(main, text = "Enter the the judgement for the votes",borderwidth=5)
    description_label.grid(row = 2, column = 0, columnspan = 3, pady = 10)
    player_description = Entry(main, width = 35)
    player_description.grid(row = 3, column = 0, columnspan = 3, pady = 10)
    description = player_description.get()

#labels

# player name and entry box

player_label = Label(main, text="Enter player name: ")
player_label.grid(row=1, column = 0, columnspan=1)
player_name = Entry(main)
player_name.grid(row = 1, column = 1, columnspan = 2, pady = 5)
player = player_name.get()

# player judgement and entry box

description_label = Label(main, text = "Enter the the judgement for the votes",borderwidth=5)
description_label.grid(row = 2, column = 0, columnspan = 3, pady = 10)
player_description = Entry(main, width = 35)
player_description.grid(row = 3, column = 0, columnspan = 3, pady = 10)
description = player_description.get()


# Buttons
submit = Button(main, text = "Submit", command = submit, padx=10)
submit.grid(row = 4, column = 0, padx = 10)

exit = Button(main, text = "Exit", command = main.quit, padx = 25)
exit.grid(row = 4, column = 1, padx = 10)

display_button = Button(main, text = "Display Judgement", command = display, padx=50)
display_button.grid(row = 5, column = 0, padx=50, pady = 25, columnspan=3)



main.mainloop()
print(player_list)
print(description_list)
