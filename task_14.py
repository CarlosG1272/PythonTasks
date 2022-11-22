import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.geometry("400x130")

# Define components for the GUI
master = ttk.Frame(window)
optionsFrame = ttk.Frame(window, borderwidth=10, relief="ridge", width=400, height=350)
description = ttk.Label(window, text="This is a simple GUI when you can select an option.")
buttonForReset = ttk.Button(window, text="Reset")

# Declare radio buttons
selectedOption = tkinter.IntVar()
rb1 = ttk.Radiobutton(optionsFrame, text="Option1", value=1, variable=selectedOption)
rb2 = ttk.Radiobutton(optionsFrame, text="Option2", value=2, variable=selectedOption)
rb3 = ttk.Radiobutton(optionsFrame, text="Option3", value=3, variable=selectedOption)
rb4 = ttk.Radiobutton(optionsFrame, text="Option4", value=4, variable=selectedOption)
rb5 = ttk.Radiobutton(optionsFrame, text="Option5", value=5, variable=selectedOption)
# Bind event with a button for reset selected radio button
def resetSelected(Event):
    global selectedOption
    selectedOption.initialize(None)
buttonForReset.bind("<Button-1>", resetSelected)

# Position the elements in the grid
rb1.grid(column=0, row=0)
rb2.grid(column=0, row=1)
rb3.grid(column=0, row=2)
rb4.grid(column=0, row=3)
rb5.grid(column=0, row=4)
master.grid(column=0, row=0)
optionsFrame.grid(column=0, row=0, columnspan=3, rowspan=2)
description.grid(column=3, row=0)
buttonForReset.grid(column=3, row=1)

window.mainloop()