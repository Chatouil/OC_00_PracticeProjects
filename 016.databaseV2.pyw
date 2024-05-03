import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from pathlib import Path
import threading
import sqlite3
import os
import sv_ttk

root = tk.Tk()
root.title("Database")
root.iconbitmap("data/icons/python1.ico")
root.geometry("400x300") 
root.minsize(400, 236)
root.resizable(False, True)

sv_ttk.set_theme("dark")

# Create DB
scriptpath = Path.cwd()
dbpath = str(scriptpath) + "\\data\\016.database.db"
print("PATH : " + dbpath)

# Check empty values
def emptyCheck(edit,id,editframe):
	entryvalues = [f_name.get(),l_name.get(),address.get(),city.get(),state.get(),zipcode.get()]
	emptyvalues = False
	for entry in entryvalues:
		#print(entry)
		if str(entry) == "":
			emptyvalues = True
	
	if emptyvalues:
			# Empty values warning
			answer = messagebox.askquestion("Question PopUp", "There's empty values, add anyway ?")
			if answer == "yes":
				if edit:
					savedit(id,editframe)
				else:
					dbsubmit()
				
			else:
				return
	else:
		if edit:
			savedit(id,editframe)
		else:
			dbsubmit()

# Submit function
def dbsubmit():
	# Connect + Cursor
	connect = sqlite3.connect(dbpath)
	cursor = connect.cursor()
	# Write data
	cursor.execute("INSERT INTO addresses VALUES (:f_name,:l_name,:address,:city,:state,:zipcode)",
		{
			"f_name": f_name.get(),
			"l_name": l_name.get(),
			"address": address.get(),
			"city": city.get(),
			"state": state.get(),
			"zipcode": zipcode.get()
		})

	# Clear text boxes
	f_name.delete(0, END)
	l_name.delete(0, END)
	address.delete(0, END)
	city.delete(0, END)
	state.delete(0, END)
	zipcode.delete(0, END)

	# Commit changes
	connect.commit()
	
	# Close connection
	connect.close()
	
	# Update display
	dbquery()

# Edit & Delete functions
def discardedit(editframe):
	submit_btn.config(state=NORMAL)
	for widget in scrollable_frame.winfo_children():
		# Enable buttons
		if isinstance(widget, Button):
			widget.config(state=NORMAL)
	
	# Kill editor buttons
	for widget in editframe.winfo_children():
		widget.destroy()
	
	editframe.destroy()
	
	# Clear text boxes
	f_name.delete(0, "end")
	l_name.delete(0, "end")
	address.delete(0, "end")
	city.delete(0, "end")
	state.delete(0, "end")
	zipcode.delete(0, "end")

# Save edited records
def savedit(id,editframe):
	# Connect + Cursor
	connect = sqlite3.connect(dbpath)
	cursor = connect.cursor()
	
	# Fetch values from entry fields
	update_f_name = f_name.get()
	update_l_name = l_name.get()
	update_address = address.get()
	update_city = city.get()
	update_state = state.get()
	update_zipcode = zipcode.get()
	
	# Update data
	cursor.execute("""UPDATE addresses SET
		f_name = :f_name,
		l_name = :l_name,
		address = :address,
		city = :city,
		state = :state,
		zipcode = :zipcode
		
		WHERE oid = :oid""",
		{
			"f_name": update_f_name,
			"l_name": update_l_name,
			"address": update_address,
			"city": update_city,
			"state": update_state,
			"zipcode": update_zipcode,
			"oid": id
		})
	
	# debug de chat gpt qui ne marche pas :
	#cursor.execute("""UPDATE addresses SET
	#				f_name = ?,
	#				l_name = ?,
	#				address = ?,
	#				city = ?,
	#				state = ?,
	#				zipcode = ?
	#			WHERE oid = ?""",
	#		   (update_f_name,update_l_name, update_address, update_city, update_state, update_zipcode, id))
	
	# Commit changes
	connect.commit()
	
	# Close connexion
	connect.close()
	
	# Reset button states
	submit_btn.config(state=NORMAL)
	for widget in scrollable_frame.winfo_children():
		if isinstance(widget, Button):
			# Do something if the widget is a Button
			# print("This widget" + str(widget) + " is a Button")
			widget.config(state=NORMAL)
	for widget in editframe.winfo_children():
		widget.destroy()
	
	editframe.destroy()
	
	# Clear text boxes
	f_name.delete(0, "end")
	l_name.delete(0, "end")
	address.delete(0, "end")
	city.delete(0, "end")
	state.delete(0, "end")
	zipcode.delete(0, "end")
	
	# Update display
	dbquery()

# Edit function, show data in boxes	
def dbedit(id):
	# Clear text boxes
	f_name.delete(0, "end")
	l_name.delete(0, "end")
	address.delete(0, "end")
	city.delete(0, "end")
	state.delete(0, "end")
	zipcode.delete(0, "end")
	
	# Connect + Cursor
	connect = sqlite3.connect(dbpath)
	cursor = connect.cursor()
	
	# Read data
	cursor.execute("SELECT * FROM addresses WHERE oid ="+str(id))
	records = cursor.fetchall()
	for record in records:
		f_name.insert(0, record[0])
		l_name.insert(0, record[1])
		address.insert(0, record[2])
		city.insert(0, record[3])
		state.insert(0, record[4])
		zipcode.insert(0, record[5])
	
	# Close connexion
	connect.close()
	
	# Disable Submit btn & all other scrollable_frame buttons
	submit_btn.config(state=DISABLED)
	for widget in scrollable_frame.winfo_children():
		if isinstance(widget, Button):
			# Do something if the widget is a Button
			# print("This widget" + str(widget) + " is a Button")
			widget.config(state=DISABLED)
	
	# Display Save & Discard buttons
	editframe = Canvas(root, borderwidth=0)
	save_btn = Button(editframe, text="Save", command=lambda:emptyCheck(True,id,editframe))
	save_btn.grid(row=0, column=0, padx=(20, 10), pady=10, sticky="ew")
	discard_btn = Button(editframe, text="Discard", command=lambda:discardedit(editframe))
	discard_btn.grid(row=0, column=1, padx=(10, 20), pady=10, sticky="ew")
	editframe.grid(row=6, column=1, sticky="ew")
	editframe.grid_columnconfigure(0, weight=1)
	editframe.grid_columnconfigure(1, weight=1)
	
	# Update display
	dbquery()

# Delete function
def dbdelete(id):
	# Connect + Cursor
	connect = sqlite3.connect(dbpath)
	cursor = connect.cursor()
	
	# Delete a record
	cursor.execute("DELETE from addresses WHERE oid="+str(id))
	print("Record id#"+str(id)+" deleted")
	
	# Commit changes
	connect.commit()
	
	# Close connection
	connect.close()
	
	# Update display
	dbquery()

# Query function
def dbquery():
	# Get rid of previous display
	for widget in scrollable_frame.winfo_children():
		widget.destroy()
	
	# Connect + Cursor
	connect = sqlite3.connect(dbpath)
	cursor = connect.cursor()
	
	# Read data
	cursor.execute("SELECT *, oid FROM addresses"),
	records = cursor.fetchall()
	for record in records:
		#print(record)
		print_records = ""
		if record[6] < 10:
			print_records += "0"
		print_records += str(record[6]) + "  |  " + str(record[0]) + " " + str(record[1])
		edit_entry = Button(scrollable_frame, text="Edit", command=lambda id=record[6]: dbedit(id), padx=0, pady=0)
		edit_entry.grid(row=record[6], column=1, padx=0, pady=0)
		delete_entry = Button(scrollable_frame, text="Delete", command=lambda id=record[6]: dbdelete(id), pady=0)
		delete_entry.grid(row=record[6], column=2, padx=0, pady=0)
		query_label = Label(scrollable_frame, text=print_records, anchor=W, justify="left", width=38, bg="green", padx=5)
		query_label.grid(row=record[6], column=0, padx=2, pady=0)
	
	# Close connexion
	connect.close()
	
	# Update scrollbar visibility
	update_scrollbar()

def update_scrollbar():
	# Get the total height of the content in the scrollable frame
	total_height = scrollable_frame.winfo_reqheight()

	# Get the height of the canvas
	canvas_height = canvas.winfo_height()

	# Check if the total height is less than or equal to the canvas height
	if total_height <= canvas_height:
		# If yes, disable the scrollbar
		scrollbar.grid_forget()
	else:
		# If no, enable the scrollbar
		scrollbar.grid(row=0, column=1, sticky="nes")

# Create table
if not Path(dbpath).is_file():
	# Connect + Cursor
	connect = sqlite3.connect(dbpath)
	cursor = connect.cursor()
	cursor.execute("""CREATE TABLE addresses (
		f_name text,
		l_name text,
		address text,
		city text,
		state text,
		zipcode integer
		)""")
	
	# Commit changes
	connect.commit()
	# Close connexion
	connect.close()

# Create text boxes
f_name = Entry(root, width=40)
l_name = Entry(root, width=40)
address = Entry(root, width=40)
city = Entry(root, width=40)
state = Entry(root, width=40)
zipcode = Entry(root, width=40)

f_name.grid(row=0, column=1, padx=20, pady=(15,0))
l_name.grid(row=1, column=1, padx=20)
address.grid(row=2, column=1, padx=20)
city.grid(row=3, column=1, padx=20)
state.grid(row=4, column=1, padx=20)
zipcode.grid(row=5, column=1, padx=20)

# Creat labels
f_name_lbl = Label(root, text="First Name", width=15)
l_name_lbl = Label(root, text="Last Name", width=15)
address_lbl = Label(root, text="Address", width=15)
city_lbl = Label(root, text="City", width=15)
state_lbl = Label(root, text="State", width=15)
zipcode_lbl = Label(root, text="Zipcode", width=15)

f_name_lbl.grid(row=0, column=0, padx=20, pady=(15,0))
l_name_lbl.grid(row=1, column=0, padx=20)
address_lbl.grid(row=2, column=0, padx=20)
city_lbl.grid(row=3, column=0, padx=20)
state_lbl.grid(row=4, column=0, padx=20)
zipcode_lbl.grid(row=5, column=0, padx=20)

# Create submit button
submit_btn = Button(root, text="Add to db", command=lambda:emptyCheck(False,"",""))
submit_btn.grid(row=6, column=1, padx=20, pady=10, ipadx=92)

## Create a Query button
#queryButton = Button(root, text="Show records", command=dbquery)
#queryButton.grid(row=7, column=1, padx=20, pady=10)

# Créer la frame contenant la scrollbar et le canvas
frame = LabelFrame(root)
frame.grid(row=8, column=0, columnspan=2, padx=10, pady=(0,10), ipady=0, sticky=NSEW)

#canvas = Canvas(frame, borderwidth=0, height=100)
canvas = Canvas(frame, borderwidth=0)

# Configure row and column to stretch
root.grid_rowconfigure(8, weight=1)  # Configure row 8 to stretch vertically
root.grid_columnconfigure(0, weight=1)  # Configure column 0 to stretch horizontally

scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas)

def _on_mousewheel(event):
	#Scrolllllll
	canvas.yview_scroll(int(-1*(event.delta/30)), "units")

def _on_canvas_configure(event):
	# Update scrollbar visibility when the canvas size changes
	update_scrollbar()

# Bind the canvas events functions
canvas.bind_all("<MouseWheel>", _on_mousewheel)
canvas.bind("<Configure>", _on_canvas_configure)

scrollable_frame.bind(
	"<Configure>",
	lambda e: canvas.configure(
		scrollregion=canvas.bbox("all")
	)
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.grid(row=0, column=0)
scrollbar.grid(row=0, column=0)

# Update display
dbquery()

root.mainloop()