from tkinter import *

root = Tk()
root.title("?")
root.iconbitmap("data/icons/python1.ico")

# Creating a Label Widget
myLabel1 = Label (root, text="Hello World!")
myLabel2 = Label (root, text="What is the meaning of life ?")

# Shoving it onscreen
myLabel1.grid(row=0, column=0, padx=10, pady=5)
myLabel2.grid(row=1, column=1, padx=10, pady=5)

root.mainloop()

# IS THE SAME AS :
# from tkinter import *
# 
# root = Tk()
# 
# myLabel1 = Label (root, text="Hello World!").grid(row=0, column=0)
# myLabel2 = Label (root, text="What is the meaning of life ?").grid(row=1, column=1)
# 
# root.mainloop()