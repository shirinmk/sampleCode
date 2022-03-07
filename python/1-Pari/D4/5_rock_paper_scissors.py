# Rock Paper Scissors
# Instructions
#
# Make a rock, paper, scissors game.
#
# Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable:
# rock, paper, and scissors. This will make it easy to print them out to the console.
#
# Start the game by asking the player:
#
# "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."
#
# From there you will need to figure out:
#
#     How you will store the user's input.
#     How you will generate a random choice for the computer.
#     How you will compare the user's and the computer's choice to determine the winner (or a draw).
#     And also how you will give feedback to the player.
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

#Write your code below this line 👇

user_choice = int( input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else:
    print(scissors)
computer_choice = random.randint(0, 2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)

if user_choice == computer_choice:
    print("drasw")
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("user wins")
elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
    print("you lost")
else:
    print("not hewr")
