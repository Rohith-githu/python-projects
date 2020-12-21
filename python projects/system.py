import getpass 
import time
print('Hi this is the 7th version of the system.py\nin this version you can try 3 times to enter the pin and has robot verification after 2nd try\nand had 5 seconds delay function in executing the function that you can cancel the function by closing the file.\n')
def system() :
    import os
    import ctypes
    # import time
    # the functions are below.
    print('1.shutdown\n2.restart\n3.signout\n4.lock\n5.sleep')
    print('\nthis would delete all the unsaved work')
    ask = input('which function do you want to run?')

    if ask == '1':
        print('this function will be executed in 5 seconds if you dont want to run the function close the file to escape the execution')
        print('\nthis would delete all the unsaved work')
        time.sleep(5)
        os.system("shutdown /s /t 1") 
    elif ask == '2':
        print('this function will be executed in 5 seconds if you dont want to run the function close the file to escape the execution') 
        print('\nthis would delete all the unsaved work')
        time.sleep(5)
        os.system("shutdown /r /t 1")
    elif ask == '3':
        print('this function will be executed in 5 seconds if you dont want to run the function close the file to escape the execution')
        print('\nthis would delete all the unsaved work')
        time.sleep(5)
        os.system("shutdown -l") 
    elif ask == '4':
        ctypes.windll.user32.LockWorkStation()
    elif ask == '5':
        print('this function will be executed in 5 seconds if you dont want to run the function close the file to escape the execution')
        time.sleep(5)
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    else :
        print('error you didnt entered the number to execute the program')
        input('type ex to exit the program')
        time.sleep(5)
        exit()
password = 'execute'
password1 = getpass.getpass(prompt='Please enter the pin to use the system.py? ') 
if password1 == password:
    # the modules 
    system()
else :
    retry = getpass.getpass(prompt='you had entered the wrong pin pls try again? ')
    if retry == password:
        system()
    elif retry != password:
        asktry = input('sorry entered wrong password')