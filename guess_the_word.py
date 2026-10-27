# Veronica Valenzuela
# CIS256 Fall 2026
# Progamming Assignment 4

""" Create a word-guessing game. """

import random

word_list = ["tree", "street", "grass", "truck", "shoes"]

""" Select word from predified list """
def get_word():
    word = random.choice(word_list)
    return word.upper()

""" Play Guess the Word game """ 
def play(word):
    word_completion = ["_"] * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6 # Number of incorrect attmpts 
    print("Let's play!")
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        # Prompts user to guess letter or word. 
        guess = input("Guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha(): 
            if guess in guessed_letters:
                print("Letter already guessed", guess)
            elif guess not in word:
                tries -= 1
                guessed_letters.append(guess)
            else:
                # Correct guess indication.
                print("Nice!", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                # Letter is revealed when guess correctly. 
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Word already guessed", guess)
            elif guess != word:
                print(guess, "is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Sorry! Guess again")

        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats, you got it!")
        # Congratulatory message for successfully guessing the word.
    else:
        print("Out of tries. The word was " + word + " thanks for playing.")

""" Restarts games, if user wants to replay """ 
def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N)").upper() == "Y":
        word = get_word()
        play(word)

""" Allows user to continue playing"""
if __name__ == "__main__":
    main()
