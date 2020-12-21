from tkinter import *

root = Tk()
# creating a label widget's
label1 = Label(root, text="Hello World")
label2 = Label(root, text="my name is rohith")
# arranging to grid
label1.grid(row = 0, column =0)
label2.grid(row = 1, column =5)

root.mainloop()