import os
inp = input('do you want to sleep your pc? (yes/no) ')
if inp == 'yes':
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    exit()
else:
    exit()