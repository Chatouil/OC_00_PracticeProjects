import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Multiple tabs")
root.iconbitmap("./data/icons/python1.ico")
root.geometry("500x500")

btnActive_color_fg = "blue"
frame_color_bg = "white"
btnInactive_color_fg = "black"
btnInactive_color_bg = "grey"

def switch(swbtn,swlbl,page):
	for items in indicators:
		items[0]["bg"] = btnInactive_color_bg
		items[0]["fg"] = btnInactive_color_fg
		items[1]["bg"] = btnInactive_color_bg
	
	swbtn["bg"] = frame_color_bg
	swbtn["fg"] = btnActive_color_fg
	swlbl["bg"] = btnActive_color_fg
	
	for frame in main_frame.winfo_children():
		frame.destroy()
		root.update()
	
	page()

options_frame = tk.Frame(root)
options_frame.pack(pady=5)
options_frame.pack_propagate(False)
options_frame.configure(width=500, height=35)

btn1 = tk.Button(options_frame, text="Home", font=("helvetica", 14), bd=0, activeforeground=btnActive_color_fg, command=lambda:switch(swbtn=btn1,swlbl=btn1_line,page=showTab1))
btn1.place(x=0,y=0,width=125)
btn1_line = tk.Label(options_frame,bg=btnActive_color_fg)
btn1_line.place(x=25,y=30,width=76,height=2)

btn2 = tk.Button(options_frame, text="Products", font=("helvetica", 14), bd=0, activeforeground=btnActive_color_fg,command=lambda:switch(swbtn=btn2,swlbl=btn2_line,page=showTab2))
btn2.place(x=125,y=0,width=125)
btn2_line = tk.Label(options_frame)
btn2_line.place(x=150,y=30,width=76,height=2)

btn3 = tk.Button(options_frame, text="Contact", font=("helvetica", 14), bd=0, activeforeground=btnActive_color_fg,command=lambda:switch(swbtn=btn3,swlbl=btn3_line,page=showTab3))
btn3.place(x=250,y=0,width=125)
btn3_line = tk.Label(options_frame)
btn3_line.place(x=275,y=30,width=76,height=2)

btn4 = tk.Button(options_frame, text="About", font=("helvetica", 14), bd=0, activeforeground=btnActive_color_fg,command=lambda:switch(swbtn=btn4,swlbl=btn4_line,page=showTab4))
btn4.place(x=375,y=0,width=125)
btn4_line = tk.Label(options_frame)
btn4_line.place(x=400,y=30,width=76,height=2)

indicators = [(btn1,btn1_line),(btn2,btn2_line),(btn3,btn3_line),(btn4,btn4_line)]
# initializing colors
indicators[0][0]["bg"] = frame_color_bg
indicators[0][0]["fg"] = btnActive_color_fg
indicators[0][1]["bg"] = btnActive_color_fg
indicators[1][0]["bg"] = btnInactive_color_bg
indicators[1][0]["fg"] = btnInactive_color_fg
indicators[1][1]["bg"] = btnInactive_color_bg
indicators[2][0]["bg"] = btnInactive_color_bg
indicators[2][0]["fg"] = btnInactive_color_fg
indicators[2][1]["bg"] = btnInactive_color_bg
indicators[3][0]["bg"] = btnInactive_color_bg
indicators[3][0]["fg"] = btnInactive_color_fg
indicators[3][1]["bg"] = btnInactive_color_bg

def showTab1():
	tab1_frame = tk.Frame(main_frame)
	tab1_label = tk.Label(tab1_frame, text="Home page content")
	tab1_label.pack(pady=80)
	tab1_frame.pack(fill=tk.BOTH, expand=True)

def showTab2():
	tab2_frame = tk.Frame(main_frame)
	tab2_label = tk.Label(tab2_frame, text="Products page content")
	tab2_label.pack(pady=80)
	tab2_frame.pack(fill=tk.BOTH, expand=True)

def showTab3():
	tab3_frame = tk.Frame(main_frame)
	tab3_label = tk.Label(tab3_frame, text="Contact page content")
	tab3_label.pack(pady=80)
	tab3_frame.pack(fill=tk.BOTH, expand=True)

def showTab4():
	tab4_frame = tk.Frame(main_frame)
	tab4_label = tk.Label(tab4_frame, text="About page content")
	tab4_label.pack(pady=80)
	tab4_frame.pack(fill=tk.BOTH, expand=True)

main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

showTab1()

root.mainloop()
