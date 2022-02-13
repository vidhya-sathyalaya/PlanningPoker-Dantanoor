from tkinter import *
root = Tk()
root.title('Planning Poker')
root.iconbitmap('/Users/vhps/PycharmProjects/ Python/search_players.py')
root.geometry("500x300")
def update(data):
	my_list.delete(0, END)
	for item in data:
		my_list.insert(END, item)
def fillout(e):
	my_entry.delete(0, END)
	my_entry.insert(0, my_list.get(ANCHOR))
def check(e):
	typed = my_entry.get()

	if typed == '':
		data = toppings
	else:
		data = []
		for item in toppings:
			if typed.lower() in item.lower():
				data.append(item)
	update(data)
my_label = Label(root, text="Search Players",
	font=("Helvetica", 14), fg="grey")
my_label.pack(pady=20)
my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack()
my_list = Listbox(root, width=50)
my_list.pack(pady=40)
toppings = ["Player 1", "Player 2", "Player 3",
	"Player 4", "Player 5", "Player 6", "Player 7", "Player 8", "Player 9", "Player 10", "Player 11", "Player 12 "]
update(toppings)
my_list.bind("<<ListboxSelect>>", fillout)
my_entry.bind("<KeyRelease>", check )
root.mainloop()