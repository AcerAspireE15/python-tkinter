# handling button clicks

from tkinter import *

root = Tk()

def dosomething():
    print("you clicked the button")

button1 = Button(root, text="CLICK HERE", command= dosomething )
button1.pack()

root.mainloop()