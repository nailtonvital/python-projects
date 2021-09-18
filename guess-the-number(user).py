import random


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    # execute a loop while the feedback isn't 'c' (correct)
    while feedback != 'c':
        if low != high:
            # generates a number between 'low' and 'high'
            guess = random.randint(low, high)
        else:
            guess = low
        # get the feedback of the user parse to lowercase
        feedback = input(f"Is {guess} high(H), low(L) or correct(C)?").lower()
        # add or remove number until get right
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Whoa! The computer guess the number {guess} correctly!")


# max interval of numbers
computer_guess(100)
