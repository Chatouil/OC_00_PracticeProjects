from tkinter import *
from PIL import ImageTk, Image
from urllib.request import urlopen

root = Tk()
root.title("ImageViewer")
root.iconbitmap("data/icons/landscapetree.ico")

# Load the original image
original_image = Image.open("data/python.jpg")
#original_image = Image.open("data/police.jpg")
#original_image = Image.open(urlopen("https://www.interieur.gouv.fr/var/miomcti/storage/images/media/police-nationale/images/logo-police-nationale-500-px/270879-2-fre-FR/Logo-police-nationale-500-px.jpg"))

# Resize the image to your desired dimensions
width, height = 400, 300
resized_image = original_image.resize((width, height))

# Convert the resized image to PhotoImage
resized_img = ImageTk.PhotoImage(resized_image)

# Create a label with the resized image
my_label = Label(image=resized_img)
my_label.pack()

root.configure(bg="#333333")
root.resizable(False,False)
root.mainloop()