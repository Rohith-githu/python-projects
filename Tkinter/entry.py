from tkinter import *

root = Tk()
# creating an simple button widget.
# here the padx and pady adjusts padding of the widget.
e = Entry(root, bg = 'white', fg = 'black', borderwidth = 5, width = 60)
e.pack()
e.insert(0, 'Enter your name:')

def letsclick():
    hello = 'hello ' + e.get()
    mylabel = Label(root, text=hello)
    mylabel.pack()
# the command attribute runs the function which is written in it.
mybutton = Button(root, text='register your name', command = letsclick, fg ='blue', bg ='#ffffff')
mybutton.pack()


root.mainloop()