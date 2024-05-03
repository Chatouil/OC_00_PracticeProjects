from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
from PIL import ImageTk, Image
from urllib.request import urlopen
from urllib import *
import threading
import time

root = Tk()
root.title("MessageBox")
root.iconbitmap("data/icons/python1.ico")

resized_img = None
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def center_window(window):
	window.update_idletasks()
	width = window.winfo_width()
	height = window.winfo_height()
	x = (window.winfo_screenwidth() - width) // 2
	y = (window.winfo_screenheight() - height) // 2
	window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def show_info():
	messagebox.showinfo("Informative PopUp", "Les poules pondent des œufs.")

def show_warning():
	messagebox.showwarning("Warning PopUp", "Le climat se dérègle, on va tous mourir !")

def show_error():
	messagebox.showerror("Error PopUp", "Error 0x80763429: File is corrupted and unreadable.")

def show_question():
	global resized_img  # Declare global variable
	answer = messagebox.askquestion("Question PopUp", "As-tu déjà enculé un mouton ?")
	if answer == "yes":
		msg = Toplevel()
		msg.title("MessageBox")
		msg.overrideredirect(True)  # Removes top bar
		label1 = Label(msg, text="WOW", padx=20, pady=10).pack()
		label2 = Label(msg, text="J'appelle la police !", padx=20, pady=5).pack()
		width, height = 150, 150
		original_image = Image.open(urlopen("https://cf-st.sc-cdn.net/aps/bolt/aHR0cHM6Ly9jZi1zdC5zYy1jZG4ubmV0L2Qvbzl2OERCV2NNQWVvVmVDelBFU1E4P2JvPUVnMGFBQm9BTWdFRVNBSlFHV0FCJnVjPTI1.jpg"))
		resized_image = original_image.resize((width, height))
		resized_img = ImageTk.PhotoImage(resized_image)
		label3 = Label(msg, image=resized_img, padx=20, pady=10).pack()
		center_window(msg)  # Center the window on the screen
		msg.after(3000, msg.destroy)  # Destroy the window after 3000 milliseconds (3 seconds)
	else:
		msg = Toplevel()
		msg.title("MessageBox")
		msg.overrideredirect(True)  # Removes top bar
		label = Label(msg, text="Tant mieux !", padx=20, pady=10)
		label.pack()
		center_window(msg)  # Center the window on the screen
		msg.after(2000, msg.destroy)  # Destroy the window after 2000 milliseconds (2 seconds)

def create_tcc(input_bar, input_progress_dialog, integer, string):
	barSpeed = 0.05
	if integer == 0:
		input_bar["maximum"] = 100
		input_bar["value"] = 0
		for x in range(input_bar["maximum"]):
			time.sleep(barSpeed)
			input_bar["value"] += 1
	else:
		input_bar["maximum"] = 100
		input_bar["value"] = 100
		for x in range(input_bar["maximum"]):
			time.sleep(barSpeed)
			input_bar["value"] -= 1
	time.sleep(1)
	label = Label(input_progress_dialog, text=string, pady=10)
	label.grid(row=5, columnspan=2)
	time.sleep(3)
	input_progress_dialog.destroy()

def run_tcc(string1,string2,integer1):
	barSize = 500
	progress_dialog = Toplevel()
	progress_dialog.title(string1)
	progress_dialog.attributes("-disabled", True)
	bar = Progressbar(progress_dialog, orient="horizontal", length=barSize, value=integer1, mode="determinate")
	bar.grid(row=4, columnspan=2)
	label = Label(progress_dialog, text=" ", pady=10)
	label.grid(row=5, columnspan=2)
	center_window(progress_dialog)  # Center the window on the screen
	t = threading.Thread(target=create_tcc, args=(bar, progress_dialog, integer1, string2))
	t.start()

def show_okcancel():
	answer = messagebox.askokcancel("Ok/Cancel PopUp", "L'application Virus.exe va être installée sur votre ordinateur.")
	if answer:
		run_tcc("Installation de Virus.exe", "Le Virus a bien été installé.", 0)
		#pass
	else:
		run_tcc("Installation de Virus.exe", "Le Virus a bien été installé.", 0)
		#pass

def show_yesno():
	answer = messagebox.askyesno("Yes/No PopUp", "Êtes-vous sûr de vouloir formater C:\\ ?")
	if answer:
		run_tcc("Formatage du disque systeme", "Le disque systeme a bien été formaté.", 100)
		#pass
	else:
		run_tcc("Formatage du disque systeme", "Le disque systeme a bien été formaté.", 100)
		#pass

infoButton = Button(root, text="Info", command=show_info, width=40, pady=10, bg="#0050ff", fg="#ffffff")
warningButton = Button(root, text="Warning", command=show_warning, width=40, pady=10, bg="#ffcc00", fg="#000000")
errorButton = Button(root, text="Error", command=show_error, width=40, pady=10, bg="#e00000", fg="#000000")
questionButton = Button(root, text="Question", command=show_question, width=40, pady=10, bg="#b800dd", fg="#ffffff")
okcancelButton = Button(root, text="Ok / Cancel", command=show_okcancel, width=40, pady=10, bg="#b800dd", fg="#ffffff")
askyesnoButton = Button(root, text="Yes / No", command=show_yesno, width=40, pady=10, bg="#b800dd", fg="#ffffff")

infoButton.pack()
warningButton.pack()
errorButton.pack()
questionButton.pack()
okcancelButton.pack()
askyesnoButton.pack()

root.mainloop()