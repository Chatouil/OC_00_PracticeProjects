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

width, height = 640, 480

resizedImg1 = origImg1.resize((width, height))
resizedImg2 = origImg2.resize((width, height))
resizedImg3 = origImg3.resize((width, height))
resizedImg4 = origImg4.resize((width, height))
resizedImg5 = origImg5.resize((width, height))

my_img1 = ImageTk.PhotoImage(resizedImg1)
my_img2 = ImageTk.PhotoImage(resizedImg2)
my_img3 = ImageTk.PhotoImage(resizedImg3)
my_img4 = ImageTk.PhotoImage(resizedImg4)
my_img5 = ImageTk.PhotoImage(resizedImg5)

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

status = Label(root, text="Image 1 of " + str(len(image_list)) + "  ", fg="#ffffff", bg="#333333", pady=5, bd=1, relief=SUNKEN, anchor=E)
my_label = Label(image=image_list[0], width=600, height=300)
my_label.grid(row=0, column=0, columnspan=3)

def forward(image_number):
	global my_label
	global button_forward
	global button_backward
	
	my_label.grid_forget()
	my_label = Label(image=image_list[image_number], width=600, height=300)
	button_back = Button(root, text="<<", command=lambda:backward(image_number-1))
	
	if image_number != 4:
		button_forwd = Button(root, text=">>", command=lambda:forward(image_number+1))
	else:
		button_forwd = Button(root, text=">>", state=DISABLED)
	
	#print("image_number : " + str(image_number) + " " + str(image_list[image_number])) 
	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forwd.grid(row=1, column=2)
	status = Label(root, text="Image " + str(image_number+1) + " of " + str(len(image_list)) + "  ", fg="#ffffff", bg="#333333", pady=5, bd=1, relief=SUNKEN, anchor=E)
	status.grid(row=3, column=0, columnspan=3, sticky=W+E)

def backward(image_number):
	global my_label
	global button_forward
	global button_backward
	
	my_label.grid_forget()
	my_label = Label(image=image_list[image_number], width=600, height=300)
	button_forwd = Button(root, text=">>", command=lambda:forward(image_number+1))
	
	if image_number != 0:
		button_back = Button(root, text="<<", command=lambda:backward(image_number-1))
	else:
		button_back = Button(root, text="<<", state=DISABLED)
	
	#print("image_number : " + str(image_number) + " " + str(image_list[image_number]))  
	my_label.grid(row=0, column=0, columnspan=3)
	button_back.grid(row=1, column=0)
	button_forwd.grid(row=1, column=2)
	status = Label(root, text="Image " + str(image_number+1) + " of " + str(len(image_list)) + "  ", fg="#ffffff", bg="#333333", pady=5, bd=1, relief=SUNKEN, anchor=E)
	status.grid(row=3, column=0, columnspan=3, sticky=W+E)

button_back = Button(root, text="<<", state=DISABLED)
button_exit = Button(root, text="Exit", command=root.quit)
button_forwd = Button(root, text=">>", command=lambda:forward(1))

button_back.grid(row=1, column=0, pady=10)
button_forwd.grid(row=1, column=2, pady=10)
button_exit.grid(row=1, column=1, pady=10)
status.grid(row=3, column=0, columnspan=3, sticky=W+E)

root.configure(bg="#333333")
root.mainloop()