import functools
import logging
import tkinter as tk
from tkinter import ttk
from sys import platform

fp = functools.partial

class ScrollableFrame(ttk.Frame):
	"""
	A scrollable frame with a scroll bar to the right, which can be moved using the mouse wheel.
	Add content to the scrollable area by making self.interior the root object.
	"""
	def __init__(self, root, *args, **kwargs):
		super().__init__(root, *args, **kwargs)

		self.grid_rowconfigure(0, weight=1)
		self.grid_columnconfigure(0, weight=1)

		# The Scrollbar, layout to the right
		self._scrollbar = ttk.Scrollbar(self, orient="vertical")
		self._scrollbar.grid(row=0, column=1, sticky="nes")

		# The Canvas which supports the Scrollbar Interface, layout to the left
		self._canvas = tk.Canvas(self, bd=0, highlightthickness=0)
		self._canvas.grid(row=0, column=0, sticky="news")

		# Bind the Scrollbar to the canvas Scrollbar Interface
		self._canvas.configure(yscrollcommand=self._scrollbar.set)
		self._scrollbar.configure(command=self.yview_wrapper)

		# Reset the view
		self._canvas.xview_moveto(0)
		self._canvas.yview_moveto(0)

		# The scrollable area, placed into the canvas
		# All widgets to be scrolled have to use this Frame as parent
		self.interior = ttk.Frame(self._canvas)
		self._canvas_frame = self._canvas.create_window(0, 0,
														window=self.interior,
														anchor=tk.NW)

		self.interior.bind("<Configure>", self._on_interior_configure)
		self._canvas.bind("<Configure>", self._on_canvas_configure)

		# Bind mousewheel when the mouse is hovering the canvas
		self._canvas.bind('<Enter>', self._bind_to_mousewheel)
		self._canvas.bind('<Leave>', self._unbind_from_mousewheel)

	def yview_wrapper(self, *args):
		logging.getLogger().debug(f"yview_wrapper({args})")
		moveto_val = float(args[1])
		new_moveto_val = str(moveto_val) if moveto_val > 0 else "0.0"
		return self._canvas.yview('moveto', new_moveto_val)

	def _on_interior_configure(self, event):
		reqwidth, reqheight = self.interior.winfo_reqwidth(), self.interior.winfo_reqheight()
		self._canvas.config(scrollregion=f"0 0 {reqwidth} {reqheight}")
		if self.interior.winfo_reqwidth() != self._canvas.winfo_width():
			self._canvas.config(width=self.interior.winfo_reqwidth())

	def _on_canvas_configure(self, event):
		logging.getLogger().debug(f"_configure_canvas")
		if self.interior.winfo_reqwidth() != self._canvas.winfo_width():
			self._canvas.itemconfigure(self._canvas_frame,
									   width=self._canvas.winfo_width())

	def _on_mousewheel(self, event, scroll=None):
		speed = 1 / 6
		if platform == "linux" or platform == "linux2":
			fraction = self._scrollbar.get()[0] + scroll * speed
		else:
			units = event.delta / 120
			fraction = self._scrollbar.get()[0] - units * speed

		fraction = max(0, fraction)
		self._canvas.yview_moveto(fraction)

	def _bind_to_mousewheel(self, event):
		if platform == "linux" or platform == "linux2":
			self._canvas.bind_all("<MouseWheel>", fp(self._on_mousewheel, scroll=-1))
			self._canvas.bind_all("<Button-5>", fp(self._on_mousewheel, scroll=1))
		else:
			self.bind_all("<MouseWheel>", self._on_mousewheel)

	def _unbind_from_mousewheel(self, event):
		if platform == "linux" or platform == "linux2":
			self._canvas.unbind_all("<Button-4>")
			self._canvas.unbind_all("<Button-5>")
		else:
			self.unbind_all("<MouseWheel>")

class App(tk.Tk):
	def __init__(self):
		super().__init__()
		self.title("Scrollable Frame Test")
		self.geometry("400x300")

		# Create a ScrollableFrame instance
		scrollable_frame = ScrollableFrame(self)
		scrollable_frame.pack(expand=True, fill="both")

		# Add some widgets to the interior of the ScrollableFrame
		for i in range(50):
			label = ttk.Label(scrollable_frame.interior, text=f"Label {i}")
			label.pack()

if __name__ == "__main__":
	App().mainloop()
