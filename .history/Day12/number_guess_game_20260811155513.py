import random
from art import logo

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


def check_guessed_number(guess, correct_number, attempts):
    if guess > correct_number:
        print("Too high!")
        return attempts - 1
    elif guess < correct_number:
        print("Too low!")
        return attempts - 1
    else:
        return attempts


def difficulty_level():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if level == "easy":
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS


def guess_the_number():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    correct_number = random.randint(1, 100)
    attempts = difficulty_level()

    while attempts > 0:
        print(f"You have {attempts} attempts remaining.")

        guessed_number = int(input("Make a guess: "))

        if guessed_number == correct_number:
            print(f"You got it! The answer was {correct_number}.")
            return

        attempts = check_guessed_number(
            guessed_number,
            correct_number,
            attempts
        )

        if attempts > 0:
            print("Guess again.")

    print(f"You've run out of guesses. The answer was {correct_number}.")


guess_the_number()