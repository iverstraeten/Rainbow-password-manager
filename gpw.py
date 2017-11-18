''' 18 Nov 2017 @author: Ivan Verstraeten ''' #====================== # imports
#======================
import tkinter as tk
import pyperclip
from tkinter import ttk, scrolledtext, Menu
from pw import genpass
from random import randint

# Create instance
win = tk.Tk()   
win.lift()
win.attributes("-topmost", 1)
win.after_idle(win.attributes,'-topmost',False)

# Add a title       
win.title("RainbowPass")

# Disable resizing the GUI
win.resizable(0,0)    

# Modify adding a Label
aLabel = ttk.Label(win, text="Password")
aLabel.grid(column=1, row=2, sticky="EW")

# Modify adding a Label
aLabel2 = ttk.Label(win, text="Password:")
aLabel2.grid(column=0, row=2, sticky="E")

#Modified Button Click Function
def Generate():
    pw_len = int(numberChosen.get())
    Generate.password = genpass(pw_len)
    aLabel.configure(text=Generate.password)
    fill="#"+("%06x"%randint(0,16777215))
    aLabel.configure(foreground=fill)

def Copy():
    pyperclip.copy(Generate.password)

# Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit()

# Adding a Button
action = ttk.Button(win, text="Generate!", command=Generate)
action.grid(column=0,row=1)

# Adding another Button
action = ttk.Button(win, text="copy to clipboard", command=Copy)
action.grid(column=1,row=1)

ttk.Label(win, text="Password lenght ").grid(column=0, row=0)

number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number,
state='readonly')
numbers_pw = [i for i in range(8,19)]
numberChosen['values'] = (numbers_pw)
numberChosen.grid(column=1, row=0)
numberChosen.current(0)

# Create a Menu Bar
menuBar = Menu(win)
win.config(menu=menuBar)

# Create Menu Items
fileMenu = Menu(menuBar)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)


# Create Menu Items
helpMenu = Menu( menuBar)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)

# Place cursor into name Entry
#======================
# Start GUI
#======================
win.mainloop()
