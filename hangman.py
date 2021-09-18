import random
from words import words
import string


def get_valid_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_words(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # track what the user was guessed

    lives = 8

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # used letters
        print("You have", lives, "left and you have already used these letters", "".join(used_letters))

        # what current word is
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word is: ", " ".join(word_list))

        # getting user input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
        elif user_letter in used_letters:
            print("You have already used this character. Please try again.")
        else:
            print("Invalid character, please try again")

    if lives == 0:
        print("You died. The word was: ", word)
    else:
        print("You guessed the word \n", word)


hangman()
