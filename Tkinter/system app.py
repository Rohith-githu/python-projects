                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                from tkinter import *
import time,os,ctypes
# create a password input box
root = Tk()
# functions needed to create
ref = Label(root, text = 'All the functions except lock will take 5 seconds confirmation if the apps are open pls close in the alloted time')
def shutdown() :
    time.sleep(5)
    os.system("shutdown /s /t 1")
    exit()
def restart() :
    time.sleep(5)
    os.system("shutdown /r /t 1")
    exit()
def lock() :
    ctypes.windll.user32.LockWorkStation()
    exit()
def sleep() :
    time.sleep(5)
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    exit()
def logoff() :
    time.sleep(5)
    os.system("shutdown -l")
    exit()
# the function buttons
lab1 = Label(root, text="       ")
shutb = Button(root, text="shutdown", command=shutdown, bg = 'white')
lab2 = Label(root, text="       ")
restb = Button(root, text="restart", command=restart, bg = 'white')
lab3 = Label(root, text="       ")
log