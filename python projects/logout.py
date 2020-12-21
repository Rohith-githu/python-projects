import os 
confirmed = input('confirmation to logout? (yes/no)')

if confirmed == "yes":
    os.system("shutdown -l") 
else:
    exit()
