                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               import os,time,ctypes
def system() :
    print('Welcome to the main function of the system file')
    print('pls enter the number of the function you need to execute')
    print('\n1.Shutdown\n2.restart\n3.signout\n4.lock\n5.sleep\n')
    maininput = input('Enter the number of the function to execute: ')
    if maininput == '1':
        print('You can cancell the function in 7 seconds')
        time.sleep(7)
        os.system('shutdown /s /t 1')
    elif maininput == '2':
        print('You can cancel the function in 7 seconds')
        time.sleep(7)
        os.system('shutdown /r /t 1')
    elif maininput == '3':
        print('You can cancel the function in 7 seconds')
        time.sleep(7)
        os.system('shutdown -l')
    elif maininput == '4':
        ctypes.windll.user32.LockWorkStation()
    elif maininput == '5':
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    else :
        print('Something went wrong')
# creating conditions for password
password = '0000'
entry = input('Enter the password : ')
if entry == password :
    system()
elif entry != password :
    print('you had entered the wrong password pls enter the password again')
    entry2 = input('Enter the password again : ')
    if entry2 == password :
        system()
    elif entry2 != password :
        print('you had entered the wrong password')
