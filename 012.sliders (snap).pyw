from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
from random import randrange
from tkinter import Label, ttk
import TKinterModernThemes as TKMT
import sv_ttk

window = TKMT.ThemedTKinterFrame("Snapping slider","azure","dark")
window.root.iconbitmap("data/icons/python1.ico")

ennemies=[1000,2000,3000,4000,5000]

def snap_to_magnetic_step(value):
	step = 1
	return round(value / step) * step

def update_value(value):
	scaled_value = snap_to_magnetic_step(float(value))
	scale.set(scaled_value)
	mylabel2.config(text=str(ennemies[scaled_value]))

ennemiesFrame = LabelFrame(window.root, text="", padx=5, pady=5)
scale = tk.Scale(ennemiesFrame, from_=0, to=4, orient="horizontal", showvalue=0, command=update_value, length=200)
rnd=randrange(5)
scale.set(rnd)
scale.grid(row=0, column=2, padx=0, pady=0)
mylabel1 = Label(ennemiesFrame, text="Number of ennemies :", anchor=W)
mylabel1.grid(row=0, column=0, padx=0, pady=0)
mylabel2 = Label(ennemiesFrame, text="1000", width=5, bd=1)
mylabel2.grid(row=0, column=1, padx=0, pady=0)
ennemiesFrame.pack()

#sv_ttk.set_theme("dark")

#button = ttk.Button(window.root, text="Toggle theme", command=sv_ttk.toggle_theme)
#button.pack()

window.root.mainloop()  
