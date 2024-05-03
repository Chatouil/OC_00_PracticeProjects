from tkinter import *

root = Tk()
root.title("?")
root.iconbitmap("data/icons/python1.ico")

# Creating a Label Widget
myLabel = Label (root, text="Hello World!", padx=90, pady=10)
# Shoving it onscreen
myLabel.pack()

root.mainloop()