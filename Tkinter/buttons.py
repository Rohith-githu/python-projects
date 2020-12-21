from tkinter import *

root = Tk()
# creating an simple buton widget.
# here the padx and pady adjusts padding of the widget.
def letclick():
    mylabel = Label(root, text='look i clicked a Button')
    mylabel.pack()
# the command attribute runs the function which is written in it.
mybutton = Button(root, text='click me', command = letclick, fg ='blue', bg ='#ffffff')
mybutton.pack()


root.mainloop()