from tkinter import *

root = Tk()
root.title("Butt On")
root.iconbitmap("data/icons/python1.ico")

def myClick():
	myLabel = Label(root, text="Look! I clicked a button!!")
	myLabel.pack()

# Creating a Button
# myButton = Button(root, text="Click Me!", state=DISABLED)
myButton = Button(root, text="Click Me!", command=myClick, padx=80,pady=10, bg="#0050ff", fg="#ffffff")
myButton.pack(padx=20, pady=20)

root.mainloop()