from tkinter import *
from gui_client_util import GUI_Helper
from fastapi import status
import json

util = GUI_Helper()
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

    justfn_data = {
            'name': player_name.get(),
            'justification': player_description.get()
        }

    response = util.send_request(method='put',
                                     route='/issue/justify',
                                     data=justfn_data)

    result_txt = ""
        #print(f"{json.dumps(json.loads(response.text), indent=4)}")

    if response.status_code == status.HTTP_200_OK:
        response_dict = json.loads(response.text)
        result_txt= "Justification added successfully"
        
    else:
        result_txt= "Received " + str(response.status_code) + " from server"
    Label(main, text=result_txt).grid(row = 5, column = 0, padx = 10)
    


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

exit = Button(main, text = "Exit", command = main.quit)
exit.grid(row = 4, column = 1, padx = 10)



main.mainloop()
print(player_list)
print(description_list)
