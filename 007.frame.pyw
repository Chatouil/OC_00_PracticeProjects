from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Frames")
root.iconbitmap("data/icons/python1.ico")

frame = LabelFrame(root, text="This is my Frame...", padx=5, pady=5, bg="#333333", fg="#ffffff")
frame.pack(padx=10, pady=10)

b0 = Button (frame, text="Don't click Here!")
b1 = Button (frame, text="Neither here !")
spacer = Label(frame, text=" ", padx=20, pady=5, bg="#333333")
b0.grid(row=0, column=0, padx=10)
b1.grid(row=0, column=2, padx=10)
spacer.grid(row=0, column=1)

root.configure(bg="#333333")
root.mainloop()