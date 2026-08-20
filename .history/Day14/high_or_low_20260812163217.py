from art import logo, vs
from game_data import data
import random

print(logo)


# Select a random person from the game data
def initial_data():
    return random.choice(data)


def game():

    # Initialize the score and game status
    score = 0
    game_over = False

    # Select the first person (A)
    compare_a = initial_data()

    # Continue the game until the user gives a wrong answer
    while not game_over:

        # Select the second person (B)
        compare_b = initial_data()

        # Make sure A and B are not the same person
        while compare_b == compare_a:
            compare_b = initial_data()

        # Display person A
        print(
            f"Compare A: {compare_a['name']}, "
            f"a {compare_a['description']}, "
            f"from {compare_a['country']}."
        )

        # Display VS symbol
        print(vs)

        # Display person B
        print(
            f"Against B: {compare_b['name']}, "
            f"a {compare_b['description']}, "
            f"from {compare_b['country']}."
        )

        # Ask the user to choose A or B
        choice = input(
            "Who has more followers? Type 'A' or 'B': "
        ).lower()

        # Determine who actually has more followers
        if compare_a["follower_count"] > compare_b["follower_count"]:
            correct_answer = "a"
        else:
            correct_answer = "b"

        # Check whether the user's answer is correct
        if choice == correct_answer:

            # Increase the score for a correct answer
            score += 1

            print(f"You're right! Current score: {score}.")

            # B becomes the new A for the next round
            compare_a = compare_b

        else:

            # End the game when the user gives a wrong answer
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True


# Start the game
game()