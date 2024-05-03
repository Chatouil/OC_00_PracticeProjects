from tkinter import *

root = Tk()
root.title("Basic scales")
root.iconbitmap("data/icons/python1.ico")
root.geometry("250x250")

vertical = Scale(root, from_=0, to=200, showvalue=0, tickinterval=100)
vertical.pack(pady=10)

horizontal = Scale(root, from_=-100, to=100, showvalue=0, tickinterval=100, length=200, orient=HORIZONTAL)
horizontal.pack(pady=10)

def save():
	my_label1.config(text=str(vertical.get()))
	my_label2.config(text=str(horizontal.get()))

my_btn = Button(root, text="Save", command=save).pack()

my_label1 = Label(root, text="")
my_label1.pack()
my_label2 = Label(root, text="")
my_label2.pack()

root.mainloop()