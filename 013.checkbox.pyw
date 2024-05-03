from tkinter import *
from random import randrange

root = Tk()
root.title("Checkbox")
root.iconbitmap("data/icons/python1.ico")

var1 = IntVar()
var2 = BooleanVar()

def show1():
	myLabel1.config(text=str(var1.get())).pack()

def show2():
	myLabel2.config(text=str(var2.get())).pack()

check1 = Checkbutton(root, text="Checkbox 1", variable=var1, padx=80, pady=10, command=show1)
check2 = Checkbutton(root, text="Checkbox 2", variable=var2, offvalue=False, onvalue=True, padx=80 ,pady=10, command=show2)



#change default status :
rnd1=randrange(1)
if rnd1 == 1:
	check1.select()
	myLabel1 = Label(root, text="1")
else:
	check1.deselect()
	myLabel1 = Label(root, text="0")

rnd2=randrange(1)
if rnd2 == 1:
	check2.select()
	myLabel2 = Label(root, text="True")
else:
	check2.deselect()
	myLabel2 = Label(root, text="False")

myLabel1.pack()
myLabel2.pack()

check1.pack()
check2.pack()

root.mainloop()

	