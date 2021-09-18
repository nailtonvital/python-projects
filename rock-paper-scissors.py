import random

user = input("Chose 'r' for rock, 'p' paper and 's' for scissors.")
computer = random.choice(['r', 'p', 's'])


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or \
            (player == 'p' and opponent == 'r'):
        return True


if computer == user:
    print("Its a tie")

if is_win(user, computer):
    print('You won!')
else:
    print('You lost')

