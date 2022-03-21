#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random

print("Welcome to the number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard' :")
computer_guess = random.randint(1,101)
print(computer_guess)
# computer_guess = random.randint(3, 9)
attempts = 5
while attempts > 0:
    print(f"You have {attempts} remaining to guess the number.")
    user_guess = int(input("Make a guess: "))
    if user_guess == computer_guess:
        print("you win!")
        break
    elif user_guess < computer_guess:
        print("Too Low!")
        #check if you have remaining attempts
        if attempts > 1:
            print("Guess again")
        else:
            print("You lose!")
    elif user_guess > computer_guess:
        print("Too High")
        if attempts > 1:
            print("Guess again")
        else:
            print("You lose!")
    else:
        print("not in the instruction")

    attempts -= 1
