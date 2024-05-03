from tkinter import *
import sys

root = Tk()
root.title("Calculatrice")
root.iconbitmap("data/icons/calculator.ico")

global clearBox, fNum, oper
clearBox = False

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

# Buttons functions
def buttonClick(number):
	global clearBox
	if (clearBox):
		e.delete(0, END)
		clearBox = False
	
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

def buttonReset():
	e.delete(0, END)

def buttonFunc(string):
	global clearBox
	global fNum
	global oper
	if (string != "="):
		firstNum = e.get()
		fNum = int(firstNum)
		oper = string
		e.delete(0, END)
	else:
		sNum = e.get()
		e.delete(0, END)
		if (oper == "+"):
			e.insert(0, (fNum + int(sNum)))
		if (oper == "-"):
			e.insert(0, (fNum - int(sNum)))
		if (oper == "*"):
			e.insert(0, (fNum * int(sNum)))
		if (oper == "/"):
			e.insert(0, (fNum / int(sNum)))
		
		clearBox = True
		del fNum
		del sNum

def buttonWip():
	return

# Define buttons
calcButton1 = Button(root, text="1", padx=49.3, pady=20, bg="#0050ff", fg="#ffffff", command=lambda: buttonClick(1))
calcButton2 = Button(root, text="2", padx=49.5, pady=20, bg="#0050ff", fg="#ffffff", command=lambda: buttonClick(2))
calcButton3 = Button(root, text="3", padx=49.3, pady=20, bg="#0050ff", fg="#ffffff", command=lambda: buttonClick(3))
calcButton4 = Button(root, text="4", padx=49.3, pady=20, bg="#0050ff", fg="#ffffff", command=lambda: buttonClick(4))
calcButton5 = Button(root, text="5", padx=49.5, pady=20, bg="#0050ff", fg="#ffffff", command=lambda: buttonClick(5))
calcButton6 = Button(root, text="6", padx=49.3, pady=20, bg="#0050ff", fg="#ffffff", command=lambda: buttonClick(6))
calcButton7 = Button(root, text="7", padx=49.3, pady=20, bg="#0050ff", fg="#ffffff", command=lambda: buttonClick(7))
calcButton8 = Button(root, text="8", padx=49.5, pady=20, bg="#0050ff", fg="#ffffff", command=lambda: buttonClick(8))
calcButton9 = Button(root, text="9", padx=49.3, pady=20, bg="#0050ff", fg="#ffffff", command=lambda: buttonClick(9))
calcButton0 = Button(root, text="0", padx=49.3, pady=20, bg="#0050ff", fg="#ffffff", command=lambda: buttonClick(0))
calcButtonFlo = Button(root, text=".", padx=50.4, pady=20, bg="#0050ff", fg="#ffffff", command=lambda: buttonWip("."))
calcButtonAdd = Button(root, text="+", padx=48.5, pady=20, bg="#0050ff", fg="#ffffff", command=lambda: buttonFunc("+"))
calcButtonSub = Button(root, text="-", padx=50.4, pady=20, bg="#0050ff", fg="#ffffff", command=lambda: buttonFunc("-"))
calcButtonMul = Button(root, text="x", padx=49.4, pady=20, bg="#0050ff", fg="#ffffff", command=lambda: buttonFunc("*"))
calcButtonDiv = Button(root, text="/", padx=49.4, pady=20, bg="#0050ff", fg="#ffffff", command=lambda: buttonFunc("/"))
calcButtonEqu = Button(root, text="=", padx=105.4, pady=20, bg="#0050ff", fg="#ffffff", command=lambda: buttonFunc("="))
calcButtonClr = Button(root, text="Reset", padx=38, pady=20, bg="#0050ff", fg="#ffffff", command=lambda: buttonReset())

# Shove buttons onscreen
calcButton1.grid(row=3, column=0)
calcButton2.grid(row=3, column=1)
calcButton3.grid(row=3, column=2)
# 
calcButton4.grid(row=2, column=0)
calcButton5.grid(row=2, column=1)
calcButton6.grid(row=2, column=2)
# 
calcButton7.grid(row=1, column=0)
calcButton8.grid(row=1, column=1)
calcButton9.grid(row=1, column=2)
# 
calcButton0.grid(row=4, column=0)
calcButtonAdd.grid(row=4, column=1)
calcButtonMul.grid(row=4, column=2)
# 
calcButtonFlo.grid(row=5, column=0)
calcButtonSub.grid(row=5, column=1)
calcButtonDiv.grid(row=5, column=2)
# 
calcButtonClr.grid(row=6, column=0)
calcButtonEqu.grid(row=6, column=1, columnspan=2)
# 

root.resizable(False,False)
root.mainloop()