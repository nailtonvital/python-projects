import random


def guess(x):
    # random_number receive a random number between 1 and the chose number
    random_number = random.randint(1, x)
    guess = 0
    # loop while the guess is different of the random number
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}:'))
        if guess < random_number:
            print('Sorry, try again, your input number was low.')
        elif guess > random_number:
            print('Sorry, try again, your input number was high.')

    print('Congratulations, you have guess the number {} correctly!'.format(random_number))


# max interval to 'discover'
guess(50)
