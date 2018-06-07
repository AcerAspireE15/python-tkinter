# making status bar

from tkinter import *

root = Tk()

def function1():
    print('Menu Item Clicked')

root = Tk()

mymenu = Menu(root)

root.config(menu=mymenu)

submenu = Menu(mymenu)

mymenu.add_cascade(label="File", menu=submenu)

submenu.add_command(label="Project", command=function1)
submenu.add_command(label="Save", command=function1)

submenu.add_separator()
submenu.add_command(label="Exit", command=function1)

newmenu = Menu(mymenu)
mymenu.add_cascade(label="Edit", menu=newmenu)
newmenu.add_command(label="Undo", command=function1)

toolbar = Frame(root)
insertbutton = Button(toolbar, text="insert Files", command=function1)
insertbutton.pack(side=LEFT, padx=2, pady=3)

printbutton = Button(toolbar, text="print", command=function1)
printbutton.pack(side=LEFT, padx=2, pady=3)

toolbar.pack(side=TOP, fill=X)

status = Label(root, text="this is the status", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)



root.mainloop()
