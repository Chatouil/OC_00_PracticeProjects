from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("ImageViewer")
root.iconbitmap("data/icons/landscapetree.ico")

# demo with single image
#my_img = ImageTk.PhotoImage(Image.open("data/python.jpg"))
#my_label = Label(image=my_img)
#my_label.pack()

origImg1 = Image.open("data/images/BAR3-5K_Loadingscreen_2.jpg")
origImg2 = Image.open("data/images/BAR4K_Loadingscreen_1.jpg")
origImg3 = Image.open("data/images/BAR4K_Loadingscreen_2.jpg")
origImg4 = Image.open("data/images/BAR4K_Loadingscreen_5.jpg")
origImg5 = Image.open("data/images/BAR4K_Loadingscreen_13B.jpg")

imgwidth = 600
imgheight = 300
framewidth = imgwidth-2
frameheight = imgheight-2

resizedImg1 = origImg1.resize((imgwidth, imgheight))
resizedImg2 = origImg2.resize((imgwidth, imgheight))
resizedImg3 = origImg3.resize((imgwidth, imgheight))
resizedImg4 = origImg4.resize((imgwidth, imgheight))
resizedImg5 = origImg5.resize((imgwidth, imgheight))

my_img1 = ImageTk.PhotoImage(resizedImg1)
my_img2 = ImageTk.PhotoImage(resizedImg2)
my_img3 = ImageTk.PhotoImage(resizedImg3)
my_img4 = ImageTk.PhotoImage(resizedImg4)
my_img5 = ImageTk.PhotoImage(resizedImg5)

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

status = Label(root, text="Image 1 of " + str(len(image_list)) + "  ", fg="#ffffff", bg="#333333", pady=5, bd=1, relief=SOLID, anchor=E)
status.grid(row=3, column=0, columnspan=3, sticky=W+E, padx=8, pady=4)
my_label = Label(image=image_list[0], width=framewidth, height=frameheight, bg="#333333")
my_label.grid(row=0, column=0, columnspan=3)

image_number = 0
image_count = len(image_list)

def whereTo(buttonPressed):
	global my_label
	global button_forward
	global button_backward
	global image_number
	global image_count
	
	if (buttonPressed == "forward"):
		if (image_number < (image_count-1)):
			image_number += 1
		else:
			image_number = 0
	else:
		if (image_number > 0):
			image_number -= 1
		else:
			image_number = 4
	
	my_label.grid_forget()
	my_label = Label(image=image_list[image_number], width=framewidth, height=frameheight, bg="#333333")
	my_label.grid(row=0, column=0, columnspan=3)
	status = Label(root, text="Image " + str(image_number+1) + " of " + str(len(image_list)) + "  ", fg="#ffffff", bg="#333333", pady=5, bd=1, relief=SOLID, anchor=E)
	status.grid(row=3, column=0, columnspan=3, sticky=W+E, padx=8, pady=4)
	
	print("image_number : " + str(image_number) + " " + str(image_list[image_number])) 

button_back = Button(root, text="<<", command=lambda:whereTo("backward"))
button_exit = Button(root, text="Exit", command=root.quit)
button_forwd = Button(root, text=">>", command=lambda:whereTo("forward"))

button_back.grid(row=1, column=0, pady=10)
button_forwd.grid(row=1, column=2, pady=10)
button_exit.grid(row=1, column=1, pady=10)

root.configure(bg="#333333")
root.resizable(False,False)
root.mainloop()