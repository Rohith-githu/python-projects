                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                # importing the modules we need.
from tkinter import *
import webbrowser

# creating the root variable
root = Tk()

# creating the widgets
label = Label(root, text="Click the buttons to open the browser of your wish", padx = 10, pady=10)
label.pack()
entry = Entry(root, width = 60)
# creating the functions
def main() :
    webbrowser.open('chrome.exe')
def main2() :
    webbrowser.open('msedge.exe')
def main3():
    webbrowser.open('firefox.exe')
def whatsapp() :
    webbrowser.open('https://web.whatsapp.com/')
def Practically() :
    webbrowser.open('https://www.practically.com/')
def tex() :
    webbrowser.open(entry.get())
# creating the buttons.
butt = Button(root, text="Chrome", fg = 'white', bg = 'black', command = main)
label2 = Label(root, text="             ")
butt2 = Button(root, text="Edge", fg = 'black', bg = 'white', command = main2)
label3 = Label(root, text="             ")
butt3 = Button(root, text="Firefox", fg = 'white', bg = 'orange', command = main3)
label4 = Label(root, text="             ")
butt4 = Button(root, text="whatsapp", fg ='green', bg = 'black', command = whatsapp)
label5 = Label(root,