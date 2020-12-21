import time
# from playsound import playsound
print("this is the 1st version of the countdon timer")
def countdown(t):   

    while t:
        mins,secs = divmod(t, 60)
        timer = '{:02d} : {:02d}'.format(mins,secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
    
label = input('enter the label?')
t = input('enter the time in seconds: ')
countdown(int(t))
print(f'the timer has {label} completed')
input('press ENTER to exit the file')