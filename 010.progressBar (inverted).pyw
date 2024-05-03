from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
from os import listdir
import tkinter as tk
import threading
import time
root = tk.Tk()
root.title("TCC Image Processing")

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() - width) // 2
    y = (window.winfo_screenheight() - height) // 2
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def create_tcc(input_bar, input_progress_dialog):
	barSpeed = 0.05
	input_bar["maximum"] = 100
	input_bar["value"] = 100
	for x in range(input_bar["maximum"]):
		time.sleep(barSpeed)
		input_bar["value"] -= 1
	# this fixes it
	time.sleep(1)
	input_progress_dialog.destroy()

def run_tcc():
	barSize = 500
	progress_dialog = Toplevel()
	progress_dialog.title("TCC Processing")
	#progress_dialog.overrideredirect(True)
	progress_dialog.attributes("-disabled", True)
	bar = Progressbar(progress_dialog, orient="horizontal", length=barSize, value=100, mode="determinate")
	bar.grid(row=4, columnspan=2)
	center_window(progress_dialog)  # Center the window on the screen
	t = threading.Thread(target=create_tcc, args=(bar, progress_dialog))
	t.start()

tcc_run_button = tk.Button(root, text="RUN", command=lambda:run_tcc())
tcc_run_button.pack()

root.mainloop()