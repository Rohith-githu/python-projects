import os

confirmed = input('please confir to restart your pc? (yes/no)')

if confirmed == "yes":
    os.system('shutdown /r /t 1') 
else:
    exit()