import Tkinter as tk

# Create instance
win = tk.Tk()

# Add window title
win.title("Python GUI")

# Disable resizing of window
#win.resizable(0,0)

# Add a modified label to the window
aLabel = tk.Label(win, text="A Label")
aLabel.grid(column=0, row=0)

# Button Click Event Function
def clickMe():
    action.configure(text='Hello {0}'.format(name.get()))

# Change Label
tk.Label(win, text='Enter a name:').grid(column=0, row=0)

# Add Textbox Entry Widget
name = tk.StringVar()
nameEntered = tk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1)

# Adding a button
action = tk.Button(win, text='Click Me!', command=clickMe)
action.grid(column=2, row=1)
# action.configure(state='disabled')

tk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = tk.Combobox(win, width=12, textvariable=number)
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

win.focus()
nameEntered.focus() # Change cursor to textbox
# Start the GUI
win.mainloop()

