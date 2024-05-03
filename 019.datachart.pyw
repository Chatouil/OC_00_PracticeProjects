import tkinter as tk
from tkinter import *
from tkinter import Label
from tkinter import ttk, messagebox
from pathlib import Path
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import os
import sv_ttk



root = tk.Tk()
root.title("Matplotlib Chart")
root.iconbitmap("./data/icons/python1.ico")
root.geometry("468x480") 
root.resizable(False, False)

def graph():
	house_prices = np.random.normal(200000,25000,5000)
	plt.hist(house_prices,bins=50)
	plt.show()
	#plt.pie(house_prices)
	#plt.show()
	#plt.stackplot(house_prices)
	#plt.show()

graph()
#my_button = Button(root, text="Graph", command=graph)
#my_button.pack()

sv_ttk.set_theme("dark")
root.mainloop()


