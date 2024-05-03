from tkinter import *
from tkinter import filedialog
import os

root = Tk()
root.title("Open a file")
root.iconbitmap("data/icons/python1.ico")

curr_directory = os.getcwd() # will get current working directory

def open():
	root.filename = filedialog.askopenfilename(initialdir=curr_directory, title="Select A File", filetypes=(("png files","*.png"),("jpg files","*.jpg"),("all files","*.*")))
	if root.filename:
		if not hasattr(open, 'my_label'):
			open.my_label = Label(root, text="")
			open.my_label.pack()
		
		file_name = root.filename.split("/") # split path in array
		open.my_label.config(text=file_name[-1]) # display only filename.extension
		open.my_label.config(text=root.filename) # display full path

myButton = Button (root, text="Browse", command=open, padx=80, pady=10, bg="#0050ff", fg="#ffffff")
myButton.pack(padx=20, pady=20)

my_label = Label(root, text="").pack()

root.mainloop()