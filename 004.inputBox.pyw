from tkinter import *
import sys

quizz = Tk()
quizz.title("Simple question")
quizz.iconbitmap("data/icons/python1.ico")

myTitle = Label (quizz, text="What's your Name ?")
myTitle.pack()

def myClick2(event=None):
    username = e.get()  # Récupérer la valeur de l'entrée
    if username:  # Vérifier si la chaîne n'est pas vide
        hello = "Hello " + username + " :)"
        output.config(text=hello)
    else:
        output.config(text="Please enter your name.")  # Message si aucun nom n'est entré

#def myClick3():
#    sys.exit()

e = Entry(quizz, width=50, borderwidth=5)
e.bind('<Return>', myClick2)  # Lier la touche "Entrée" à myClick2
e.pack()

myButton1 = Button (quizz, text="Send", command=myClick2, padx=50, pady=10, bg="#0050ff", fg="#ffffff")
myButton1.pack()
myButton2 = Button (quizz, text="Quit", command=quizz.quit, padx=50, pady=5, bg="#000000", fg="#ffffff")
myButton2.pack()
output = Label(quizz)
output.pack()

quizz.mainloop()