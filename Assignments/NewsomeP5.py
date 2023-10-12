# NewsomeP5
# Programmer: Corrigan Newsome
# Email: cnewsome2@cnm.edu
# Purpose: Utlizing dictionary in Python to translate a language.

import random

# a.	Initialize an empty list which you will use to store the results of each game.
tallies = {
    "user_wins": 0,
    "user_losses": 0,
    "computer_wins": 0,
    "computer_losses": 0,
    "ties": 0,
}
#  Start a game of rock paper scissors with to user.
greeting = "Welcome to the Rock Paper Scissors Game."
print(greeting)

game_pieces = ["rock", "paper", "scissors"]

computers_choice = random.choice(game_pieces)

# Ask the user to select his/her choice (rock, paper, scissors)
users_choice = input("Choose Rock, Paper or Scissors: ")

if users_choice == computers_choice:
    print(f"Both players selected  {users_choice}. It's a tie.")
    tallies["ties"] += 1
elif users_choice.lower() == "rock":
    if computers_choice == "scissors":
        print("Rock smashes scissors. You Win!!")
        tallies["user_wins"] += 1
        tallies["computer_losses"] += 1
    else:
        print("Paper covers rock! You lose")
        tallies["user_losses"] += 1
        tallies["computer_wins"] += 1

elif users_choice.lower() == "paper":
    if computers_choice == "rock":
        print("Paper covers rock. You Win!!")
        tallies["user_wins"] += 1
        tallies["computer_losses"] += 1
    else:
        print("Scissors cuts paper! You lose")
        tallies["user_losses"] += 1
        tallies["computer_wins"] += 1

elif users_choice.lower() == "scissors":
    if computers_choice == "paper":
        print("Scissors cuts paper! You Win!!")
        tallies["user_wins"] += 1
        tallies["computer_losses"] += 1
    else:
        print("Rock smashes scissors. You lose")
        tallies["user_losses"] += 1
        tallies["computer_wins"] += 1

# v.	Your program will evaluate who won or if there was a tie.

# vi.	The program reports what the computer chose, the user’s choice, who won that round, and game tally. The game tally shows number of rounds, wins/losses for the player and number of ties.

# vii.	Ask the player if the user wants to play again.

# c.	When done display a goodbye message.
