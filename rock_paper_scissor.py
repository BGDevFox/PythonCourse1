import random

computer_choice = random.choice(['rock', 'paper', 'scissors'])
human_choice = input('choose one: rock, paper or scissors \n')

if computer_choice == human_choice:
    print('TIE')
elif human_choice == 'rock' and computer_choice == 'scissors':
    print('WIN, the computer choise was ' + computer_choice)
elif human_choice == 'paper' and computer_choice == 'rock':
    print('WIN, the computer choise was ' + computer_choice)
elif human_choice == 'scissors' and computer_choice == 'paper':
    print('WIN, the computer choise was ' + computer_choice)
else:
    print('You lose, the computer choise was ' + computer_choice)