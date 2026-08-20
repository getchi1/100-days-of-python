import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
user_choice = int(input('What do you choose? '
                    'Type 0 for Rock, 1 for Paper or 2 for Scissors. \n'))
if user_choice >=0 and user_choice <= 2:
    print(game_images[user_choice])

computer_choice = random.randint(0,2)
print("Computer chose: \n", computer_choice)
print(game_images[computer_choice])

if user_choice >=3 or computer_choice < 0:
    print("You entered invalid option. Please try again.")
elif user_choice > computer_choice: #user=2 and computer=0 also user=1 and computer=0
    print("You won")
elif user_choice < computer_choice: #user=0 and computer=1 also user=1 and computer=2
    print("You lost")
elif user_choice == computer_choice:
    print("it's a draw")
elif user_choice == 0 and computer_choice == 2:
    print("You won")
elif user_choice == 2 and computer_choice == 0:
    print("You lost")







