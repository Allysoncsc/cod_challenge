
import random


def guess_number():
    random_number = random.randint(1,10)
    guess = 0
    while guess != random_number:
        guess = int(input('Guess a number between 1 and 10: '))
        if guess < random_number:
            print('Sorry, guess again. Too low. ')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')


    print(f'Yay, congrats. You have guessed the number: {random_number}')

guess_number()












