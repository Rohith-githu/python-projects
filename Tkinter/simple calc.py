                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               from tkinter import *

root = Tk()
root.title("Simple calculator")

e = Entry(root, width = 35, borderwidth = 5)
e.grid(row = 0,column = 0, columnspan = 3, padx = 10, pady = 10)

def buttonclick(number) :
    # e.delete(0, END)
    # current = e.get()
    # e.delete(0, END)
    # e.insert(0, str(current) + str(number))

def clear() :
    # e.delete(0, END)

def buttonadd() :
    # global firstnum
    # firstnum = e.get()
    # global fnum
    # fnum = int(firstnum)
    # e.delete(0, END)

print('debug24')

def buttonequal() :
    secondnum = e.get()
    e.delete(0, END)
    e.insert(0, fnum + int(secondnum))
    # return type(secondnum)

print('debug29')

butt1 = Button(root, text = '1', padx = 40, pady = 20, command = lambda : buttonclick(1))
butt2 = Button(root, text = '2', padx = 40, pady = 20, command = lambda : buttonclick(2))
butt3 = Button(root, text = '3', padx = 40, pady = 20, command = lambda : buttonclick(3))
butt4 = Button(root, text = '4', padx = 40, pady = 20, command = lambda : buttonclick(4))
butt5 = Button(root, text = '5', padx = 40, pady = 20, command = lambda : buttonclick(5))
butt6 = Button(root, text = '6', padx = 40, pady = 20, command = lambda : buttonclick(6))
butt7 = Button(root, text = '7', padx = 40, pady = 20, command = lambda : buttonclick(7))
butt8 = Button(root, text = '8', padx = 40, pady = 20, command = lambda : buttonclick(8))
butt9 = Button(root, text = '9', padx = 40, pady = 20, command = lambda : buttonclick(9))
butt0 = Button(root, text = '0', padx = 40, pady = 20, command = lambda : buttonclick(0))
print('debug40')
buttad = Button(root, text = '+', padx = 39, pady = 20, command = buttonadd())
print('debug42')
butteq = Button(root, text = '=', padx = 91, pady = 20, command = buttonequal())
buttcl = Button(root, text = 'Clear', padx = 79, pady = 20, command = clear())
# put t