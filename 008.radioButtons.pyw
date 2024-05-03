from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title("RadioButtons")
root.iconbitmap("data/icons/python1.ico")


## First Way to do it
frame1 = LabelFrame(root, text="Frame 1", padx=5, pady=5, bg="#333333", fg="#ffffff")
frame1.grid(row=0, column=0, padx=10, pady=10, sticky=N)

rb1 = IntVar()
rb1.set(0)

def clicked1(value):
	global myLabel1
	myLabel1.forget()
	myLabel1 = Label(frame1, text="You choose " + str(value), bg="#333333", fg="#ffffff")
	myLabel1.pack()

Radiobutton(frame1, text="Option1", bg="#333333", fg="#ffffff", variable=rb1, value=1, command=lambda: clicked1(1)).pack(padx=10)
Radiobutton(frame1, text="Option2", bg="#333333", fg="#ffffff", variable=rb1, value=2, command=lambda: clicked1(2)).pack(padx=10)
Radiobutton(frame1, text="Option3", bg="#333333", fg="#ffffff", variable=rb1, value=3, command=lambda: clicked1(3)).pack(padx=10)
Radiobutton(frame1, text="Option4", bg="#333333", fg="#ffffff", variable=rb1, value=4, command=lambda: clicked1(4)).pack(padx=10)

myLabel1 = Label(frame1, text="Choose option", bg="#333333", fg="#ffffff")
myLabel1.pack()

## Second Way to do it
style1=ttk.Style()
style1.map(
"design1.Toolbutton", background=[("selected", "white"), ("active","red"), ("!disabled","blue")], foreground=[("selected", "blue"), ("active","lightyellow"), ("!disabled","white")], font=[("!disabled","arial 16 bold")])

outerframe = LabelFrame(root, text="Frame 2", padx=5, pady=5, bg="#333333", fg="#ffffff")
outerframe.grid(row=0, column=1, padx=10, pady=10, sticky=N)

frame2 = LabelFrame(outerframe, text=" ", padx=5, pady=5, bg="#333333", fg="#ffffff")
frame2.grid(row=0, column=0, padx=10, pady=0, sticky=N)


rb2 = IntVar()
rb2.set(0)

def clicked2(value):
	global myLabel2
	myLabel2.forget()
	myLabel2 = Label(frame2, text="You choose " + str(value), bg="#333333", fg="#ffffff")
	myLabel2.pack()

radiobutton1=ttk.Radiobutton(frame2, text="Option1", command=lambda: clicked2(1), variable=rb2, value=1, style="design1.Toolbutton", width=20, padding=20)
radiobutton2=ttk.Radiobutton(frame2, text="Option2", command=lambda: clicked2(2), variable=rb2, value=2, style="design1.Toolbutton", width=20, padding=20)
radiobutton3=ttk.Radiobutton(frame2, text="Option3", command=lambda: clicked2(3), variable=rb2, value=3, style="design1.Toolbutton", width=20, padding=20)
radiobutton4=ttk.Radiobutton(frame2, text="Option4", command=lambda: clicked2(4), variable=rb2, value=4, style="design1.Toolbutton", width=20, padding=20)
radiobutton1.pack(padx=10, pady=1)
radiobutton2.pack(padx=10, pady=1)
radiobutton3.pack(padx=10, pady=1)
radiobutton4.pack(padx=10, pady=1)

myLabel2 = Label(frame2, text="Choose option", bg="#333333", fg="#ffffff")
myLabel2.pack()

## same, different style
style2=ttk.Style()
style2.map("design2.Toolbutton", background=[("selected", "green"), ("active","pink"), ("!disabled","grey")], foreground=[("selected", "pink"), ("active","white"), ("!disabled","green")], font=[("!disabled","arial 16 bold")])
frame3 = LabelFrame(outerframe, text=" ", padx=5, pady=5, bg="#333333", fg="#ffffff")
frame3.grid(row=1, column=0, padx=10, pady=0, sticky=N)

rb3 = IntVar()
rb3.set(0)

def clicked3(value):
	global myLabel3
	myLabel3.forget()
	myLabel3 = Label(frame3, text="You choose " + str(value), bg="#333333", fg="#ffffff")
	myLabel3.pack()

radiobutton5=ttk.Radiobutton(frame3, text="Option1", command=lambda: clicked3(1), variable=rb3, value=1, style="design2.Toolbutton", width=20, padding=20)
radiobutton6=ttk.Radiobutton(frame3, text="Option2", command=lambda: clicked3(2), variable=rb3, value=2, style="design2.Toolbutton", width=20, padding=20)
radiobutton7=ttk.Radiobutton(frame3, text="Option3", command=lambda: clicked3(3), variable=rb3, value=3, style="design2.Toolbutton", width=20, padding=20)
radiobutton8=ttk.Radiobutton(frame3, text="Option4", command=lambda: clicked3(4), variable=rb3, value=4, style="design2.Toolbutton", width=20, padding=20)
radiobutton5.pack(padx=10, pady=1)
radiobutton6.pack(padx=10, pady=1)
radiobutton7.pack(padx=10, pady=1)
radiobutton8.pack(padx=10, pady=1)

myLabel3 = Label(frame3, text="Choose option", bg="#333333", fg="#ffffff")
myLabel3.pack()

#Other Way to do it (with a loop)
style3=ttk.Style()
style3.map("design3.Toolbutton", background=[("selected", "grey"), ("active","white"), ("!disabled","orange")], foreground=[("selected", "orange"), ("active","grey"), ("!disabled","white")], font=[("!disabled","arial 16 bold")])
frame4 = LabelFrame(root, text="Frame 3", padx=5, pady=5, bg="#333333", fg="#ffffff")
frame4.grid(row=0, column=2, padx=10, pady=10, rowspan=2, sticky=N)

#rb4 = IntVar()
#rb4.set(0)

PIZZAS = [
	("Printanière","Printanière"),
	("Napolitaine","Napolitaine"),
	("Margherita","Margherita"),
	("Trois Fromages","Trois Fromages"),
	("Forestière","Forestière"),
	("Marinière","Marinière"),
	("Paysanne","Paysanne"),
	("Montagnarde","Montagnarde"),
]

pizza = StringVar()
pizza.set(" ")

def clicked4(value):
	global myLabel4
	myLabel4.forget()
	myLabel4 = Label(frame4, text="You choose " + str(value), bg="#333333", fg="#ffffff")
	myLabel4.pack()

for text, pizzaName in PIZZAS:
    radiobutton = ttk.Radiobutton(
        frame4,
        text=text,
        command=lambda pizzaName=pizzaName: clicked4(pizzaName),
        variable=pizza,
        value=pizzaName,
        style="design3.Toolbutton",
        width=20,
        padding=20,
    )
    radiobutton.pack(padx=10, pady=4)

myLabel4 = Label(frame4, text="Choose pizza", bg="#333333", fg="#ffffff")
myLabel4.pack()


root.configure(bg="#333333")
root.resizable(False,False)
root.mainloop()