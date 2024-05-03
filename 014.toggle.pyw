from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image
from pathlib import Path
import configparser
import os
import random
import sv_ttk

def toggle(button):
	if button.is_on:
		button.is_on = False
		button.configure(image=off_img, command=lambda: toggle(button))
		print("Toggle OFF")
	else:
		button.is_on = True
		button.configure(image=on_img, command=lambda: toggle(button))
		print("Toggle ON")

def togglernd(button):
	if button.is_on:
		button.is_on = False
		button.configure(image=rndoff_img, command=lambda: togglernd(button))
		print("Toggle OFF")
	else:
		button.is_on = True
		button.configure(image=rndon_img, command=lambda: togglernd(button))
		print("Toggle ON")

def save_changes():
	# ConfigParser
	config = configparser.ConfigParser()

	# Ajouter les valeurs des boutons à la section DEFAULT avec les noms originaux
	for (name, initial_value, modified, button), rnd_button in zip(new_data_array, rndbuttons):
		# Vérifier si la valeur aléatoire est activée et si le bouton aléatoire a été modifié manuellement
		if rnd_button.is_on :
			config.set("DEFAULT", name, "random")
		else:
			# Si la valeur n'est pas "random" ou si le bouton aléatoire a été désactivé,
			# enregistrer la valeur actuelle du bouton de valeur
			config.set("DEFAULT", name, "1" if button.is_on else "0")

	# Enregistrer les changements dans le fichier INI
	with open("data/014.toggle.ini", "w") as configfile:
		config.write(configfile)
	print("Changes saved.")


root = Tk()
root.title("Toggle Buttons")
root.iconbitmap("data/icons/python1.ico")

# Charger les images et les redimensionner
on_img = Image.open("data/toggle1.png").resize((36, 20), Image.LANCZOS)
off_img = Image.open("data/toggle0.png").resize((36, 20), Image.LANCZOS)
rndon_img = Image.open("data/toggleRnd1.png").resize((20, 20), Image.LANCZOS)
rndoff_img = Image.open("data/toggleRnd0.png").resize((20, 20), Image.LANCZOS)

# Convertir les images en format compatible avec tkinter
on_img = ImageTk.PhotoImage(on_img)
off_img = ImageTk.PhotoImage(off_img)
rndon_img = ImageTk.PhotoImage(rndon_img)
rndoff_img = ImageTk.PhotoImage(rndoff_img)

# Lire le fichier INI et remplir l'array new_data_array avec les noms et les données du fichier INI
bkgcolor = "#f0f0f0"
old_data_array = []
new_data_array = []
ini_file_path = "data/014.toggle.ini"
if Path(ini_file_path).is_file():
	config = configparser.ConfigParser()
	config.read(ini_file_path)
	for key in config["DEFAULT"]:
		value = config["DEFAULT"][key]
		old_data_array.append((key, value))
		if value == "random":
			value = random.choice(["0", "1"])  # Choisir aléatoirement entre 0 et 1
		modified = False  # Indicateur pour suivre si le bouton a été modifié par l'utilisateur
		new_data_array.append((key, value, modified, None))
		
		if key == "darktheme" and value == "1":
			sv_ttk.set_theme("dark")
			bkgcolor = "#1c1c1c"

# Titre de la première frame
leftframe = ttk.Frame(root, relief="solid")
label0 = Label(leftframe, text="Default settings", font="Helvetica 12 bold", padx=5, pady=5)
label0.grid(row=0, column=0, padx=5, pady=5)

# Créer les boutons basculants avec une boucle for
default_realnames = ["Dark theme","Team mode","Survival mode","Spectate mode","Limit factions","Enable Legion","Slope unifier","Reverse gear","Disable fog of war"]
buttons = []
for i, (name, value, modified, _) in enumerate(new_data_array, start=1):
    label = Label(leftframe, text=default_realnames[i-1], font="Helvetica 10", padx=0, pady=0)
    label.grid(row=i, column=0, padx=0, sticky=E)

    toggle_button = Button(leftframe, border=0, relief=SUNKEN, activebackground=bkgcolor)
    toggle_button.is_on = value == "1"  # Activer ou désactiver le bouton en fonction de la valeur dans le fichier INI
    toggle_button.configure(image=on_img if value == "1" else off_img, command=lambda button=toggle_button: toggle(button))
    toggle_button.grid(row=i, column=1, padx=4, pady=1, sticky=E)
    buttons.append(toggle_button)
    new_data_array[i-1] = (name, value, modified, toggle_button)  # Associer le bouton à ses données dans l'array

# Créer les boutons aléatoires avec une boucle for
rndbuttons = []
for i, (name, value) in enumerate(old_data_array, start=1):
    toggle_rnd_button = Button(leftframe, border=0, relief=SUNKEN, activebackground=bkgcolor)
    toggle_rnd_button.is_on = value == "random"  # Activer ou désactiver le bouton aléatoire en fonction de la valeur dans le fichier INI
    toggle_rnd_button.configure(image=rndon_img if value == "random" else rndoff_img, command=lambda button=toggle_rnd_button: togglernd(button))
    toggle_rnd_button.grid(row=i, column=2, padx=0, pady=1, sticky=W)
    rndbuttons.append(toggle_rnd_button)  # Assurez-vous d'ajouter le bouton aléatoire à la liste

    spacer = Label(leftframe, width=1, height=0)
    spacer.grid(row=i, column=3, padx=2)

spacer = Label(leftframe, font=("", 2))
rowNbr = len(new_data_array) + 1
spacer.grid(row=rowNbr, column=0)

# Créer le bouton "Save"
save_button = Button(leftframe, text="Save", command=save_changes)
save_button.grid(row=rowNbr + 1, column=1, padx=4, pady=10, sticky=W)

leftframe.grid(column=0, row=0, padx=2, pady=2)
root.mainloop()