# message box

from tkinter import *
import tkinter.messagebox

root = Tk()
tkinter.messagebox.showinfo("Title","this is awesome")


response = tkinter.messagebox.askquestion("question1","Do you like coffee")

if response == 'yes':
    print("Here is a coffee for you")
    

root.mainloop()