#import tkinter as tk
#from tkinter import Label, ttk
#root = tk.Tk()
#root.tk.call("source", "azure.tcl")
#root.tk.call("set_theme", "dark")
#root.geometry("300x300")
#L1 = Label(root, text="Hello world")
#L1.grid(row=1, column=1)
#root.mainloop()

import tkinter as tk
from tkinter import Label, ttk
import TKinterModernThemes as TKMT
window = TKMT.ThemedTKinterFrame("%yourProjectName","azure","dark")
window.root.geometry("300x300")
L1 = Label(window.root, text="Hello world")
L1.grid(row=1, column=1)
window.root.mainloop()  