import tkinter as tk
from tkinter import *
from tkinter import ttk
import sv_ttk

root = tk.Tk()
root.title("Drop Down Menu")
root.iconbitmap("data/icons/python1.ico")

sv_ttk.set_theme("dark")

myLabel = Label(root, text=" ")
myLabel.grid(row=2, column=0)

def show():
    global myLabel
    myLabel.forget()
    myLabel = Label(root, text=(var1.get()) + " " + (var2.get()))
    myLabel.grid(row=1, column=0)

optionList1 = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

optionList2 = [
    "des patates",
    "des haricots",
    "des carottes",
    "des petits pois",
    "des brocolis",
    "des andives",
    "des tomates"
]

var1 = StringVar()
var1.set(optionList1[0])

var2 = StringVar()
var2.set(optionList2[0])

dropMenu1 = OptionMenu(root, var1, *optionList1)
dropMenu1.config(width=20)
dropMenu1.grid(row=0, column=0, padx=2, pady=2, sticky="ew")

dropMenu2 = ttk.Combobox(root, textvariable=var2, values=optionList2, state="readonly")
dropMenu2.config(width=20)
dropMenu2.grid(row=0, column=1, padx=2, pady=2, sticky="ew")

myButton = Button(root, text="Show selection", command=show)
myButton.grid(row=1, column=1)

root.mainloop()