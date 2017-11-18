''' 18 Nov 2017 @author: Ivan Verstraeten ''' 
#====================== # imports #======================
import tkinter as tk
import pyperclip
from tkinter import ttk, scrolledtext, Menu
from pw import genpass
from random import randint

# create instance
win = tk.Tk()   
win.lift()
win.attributes("-topmost", 1)
win.after_idle(win.attributes,'-topmost', False)

# Add a title       
win.title("RainbowPass")

# Disable resizing the GUI
win.resizable(0,0)    

# Tab Control introduced here -----------------------------------------
tabControl = ttk.Notebook(win)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Create a tab
tabControl.add(tab1, text='Generator')      # Add the tab
tabControl.pack(expand=1, fill="both")  # Pack to make visible

tab2 = ttk.Frame(tabControl)            # Create a tab
tabControl.add(tab2, text='Storage')      # Add the tab
tabControl.pack(expand=1, fill="both")  # Pack to make visible


# ~ Tab Control introduced here -----------------------------------------
monty = ttk.LabelFrame(tab1, text="Rainbow Password Manager v1")
monty.grid(column=0, row=0, padx=8, pady=4)

# Modify adding a Label
aLabel = ttk.Label(monty, text="Password")
aLabel.grid(column=1, row=2, sticky="W")

# Modify adding a Label
aLabel2 = ttk.Label(monty, text="Password:")
aLabel2.grid(column=0, row=2, sticky="W")

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
action = ttk.Button(monty, text="Generate!", command=Generate)
action.grid(column=0,row=3)

# Adding another Button
action = ttk.Button(monty, text="copy to clipboard", command=Copy)
action.grid(column=1,row=3)

# Adding another Label
ttk.Label(monty, text="Password lenght ").grid(column=0, row=0, sticky="W")

number = tk.StringVar()
numberChosen = ttk.Combobox(monty, width=12, textvariable=number,
state='readonly')
numbers_pw = [i for i in range(8,19)]
numberChosen['values'] = (numbers_pw)
numberChosen.grid(column=1, row=0)
numberChosen.current(0)

# create a container to hold labels
# labelsFrame = ttk.LabelFrame(monty, text=" Labels in a frame ")
# labelsFrame.grid(column=0, row=7)
# 
# ttk.Label(labelsFrame, text="label1").grid(column=0, row=0)
# ttk.Label(labelsFrame, text="label2").grid(column=0, row=1)
# ttk.Label(labelsFrame, text="label2").grid(column=0, row=2)
# 
# for child in labelsFrame.winfo_children():
#     child.grid_configure(padx=8,pady=1)
# 
# 
# Place cursor into name Entry
#======================
# Start GUI
#======================
win.mainloop()
