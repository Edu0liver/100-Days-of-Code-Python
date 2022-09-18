import random
from art import logo

print('\nWellcome to the Number Guessing Game!')
print('I\'m thinking of a number between 1 and 100.')
difficult = input('\nChoose a difficulty. Type "easy" or "hard": ')

print(logo)

lives = 0

if difficult == 'easy':
    lives = 10
else:
    lives = 5

right_answer = random.randint(1, 100)

for i in range(0, lives):
    guess = int(input('\nGuess the number: '))

    if guess == right_answer:
        print(f'You got it! The answer was {right_answer}')
        break
    elif guess > right_answer:
        print('Too high.')
        print(f'You have {lives - i} attempts remaining to guess the number.')
        print('Guess again.')
    else:
        print('Too low.')
        print('Guess again.')
