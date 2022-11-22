import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.geometry("610x350")

# Define components for the GUI
master = ttk.Frame(window)
optionsFrame = ttk.Frame(window, borderwidth=10, relief="ridge", width=400, height=350)
title = ttk.Label(window, text="SIMPLE GUI FOR OPEN BOOTCAMP")
description = ttk.Label(window, text="This is a simple checkbox for determine what is your favorite programming language.")
label_listbox = ttk.Label(optionsFrame, text="Programming languages")

# Create a checkbox and define the options.
options = ("Python", "Java", "JavaScript", "C++", "Go", "Ruby", "Flutter")
list_options = tkinter.Variable(value=options)
list_box = tkinter.Listbox(optionsFrame, height=20, listvariable=list_options)

# Position the elements in the grid


master.grid(column=0, row=0)
optionsFrame.grid(column=0, row=0, columnspan=3, rowspan=2)
label_listbox.grid(column=0, row=0)
list_box.grid(column=0, row=1)
title.grid(column=3, row=0)
description.grid(column=3, row=1)
window.mainloop()