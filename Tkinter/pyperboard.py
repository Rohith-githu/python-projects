import pyperclip
from tkinter import *

root = Tk()
root.title('clipboard')
lab1 = Label(root, text="           ")
lab2 = Label(root, text="           ")
lab3 = Label(root, text="           ")
lab4 = Label(root, text="           ")
def cli():
    pyperclip.copy(inte.get())

inte = Entry(root, width = 30)
def erase():
    inte.delete(0, END)
ceat = Button(root, text = 'Copy', command = cli)
ers = Button(root, text = 'Clear', command = erase)

lab1.pack()
inte.pack()
lab2.pack()
lab4.pack()
ceat.pack()
lab3.pack()
ers.pack()

root.mainloop()