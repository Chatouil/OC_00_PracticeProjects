from tkinter import *
from tkinter import ttk

root = Tk()
root.resizable(False, False)
root.title("Scrollbar Widget Example")

# Appliquer la mise en page grid
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)


frame1 = LabelFrame(root, height=10, padx=10, pady=10)
frame1.grid(row=0, column=0, sticky=EW)
spacer = Label(frame1, text= "", height=2, padx=10, pady=10)
spacer.pack()

# Créer la frame contenant la scrollbar et le canvas
frame2 = LabelFrame(root, height=10, padx=0, pady=0)
frame2.grid(row=1, column=0, sticky=EW)

canvas = Canvas(frame2, borderwidth=0, height=100)
scrollbar = ttk.Scrollbar(frame2, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas)

def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/30)), "units")

canvas.bind_all("<MouseWheel>", _on_mousewheel)

scrollable_frame.bind(
	"<Configure>",
	lambda e: canvas.configure(
		scrollregion=canvas.bbox("all")
	)
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Ajouter du texte à la frame pour montrer le défilement
for i in range(1, 50):
	Label(scrollable_frame, text=f"Line {i}").pack()

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()