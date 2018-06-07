# using classes

from tkinter import *



class MyButtons:

    def __init__(self, rootone):

        frame = Frame(rootone)
        frame.pack()

        self.printbutton = Button(frame, text="CLICK HERE", command=self.printmessage)
        self.printbutton.pack()

        self.quitbutton = Button(frame, text="EXIT", command=frame.quit)
        self.quitbutton.pack(side=LEFT)

    def printmessage(self):
        print("BUTTON CLICKED")

root = Tk()

b = MyButtons(root)


root.mainloop()