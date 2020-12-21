import random

print('Welcome to the rock paper sissors game ')
print('Rules for the game are : \n1.rock vs paper > paper wins \n2.rock vs sissors > rock wins \n3.paper vs sissors > sissors wins')

while True:
    user_score = 0
    computer_score = 0
    ask_user = input('Enter your choice: ')
    computer_choice = random.choice(['sissors', 'rock', 'paper'])
    print(f'{computer_choice}')

    if 'rock' in ask_user and computer_choice == 'sissors' :
        print('you win!')
        user_score += 1
    elif 'rock' in ask_user and computer_choice == 'paper' :
        print('you lose!')
        computer_score += 1
    elif 'sissors' in ask_user and computer_choice == 'paper' :
        print('you win!')
        user_score += 1
    elif 'paper' in ask_user and computer_choice == 'sissors' :
        print('you lose!')
        computer_score += 1
    elif 'paper' in ask_user and computer_choice == 'rock' :
        print('you win!')
        user_score += 1
    elif 'sissors' in ask_user and computer_choice == 'rock' :
        print('you lose!')
        computer_score += 1
    elif ask_user == computer_choice:
        print('Its drawn!')
    else :
        print('Enter a valid answer')
