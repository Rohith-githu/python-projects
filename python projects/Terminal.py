import os
print('NXT Terminal')
print('created on 2020/12/01, and last update 2020/12/01')
print('copyright \'made with Python os library\'')
while True:
    # path = os.system('echo %cd%')
    command_input = input('>>>')
    os.system(command_input)