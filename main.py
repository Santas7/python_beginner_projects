# Rock, Paper, Scissors is a minigame that can be played alone with a computer.
# The game is played by two players, one of which is the computer.
# The game is played by choosing one of the three options: rock, paper or scissors.
# The rules are simple:
# 1. Rock beats scissors
# 2. Scissors beats paper
# 3. Paper beats rock

import random

# The function that will be called when the user chooses rock
def rock():
    # The computer chooses a random option
    computer = random.choice(["rock", "paper", "scissors"])
    # If the computer chooses rock
    if computer == "rock":
        # The game is a draw
        print("Computer chose rock. It's a draw!")
    # If the computer chooses paper
    elif computer == "paper":
        # The computer wins
        print("Computer chose paper. You lose!")
    # If the computer chooses scissors
    else:
        # The user wins
        print("Computer chose scissors. You win!")

# The function that will be called when the user chooses paper
def paper():
    # The computer chooses a random option
    computer = random.choice(["rock", "paper", "scissors"])
    # If the computer chooses rock
    if computer == "rock":
        # The user wins
        print("Computer chose rock. You win!")
    # If the computer chooses paper
    elif computer == "paper":
        # The game is a draw
        print("Computer chose paper. It's a draw!")
    # If the computer chooses scissors
    else:
        # The computer wins
        print("Computer chose scissors. You lose!")

# The function that will be called when the user chooses scissors
def scissors():
    # The computer chooses a random option
    computer = random.choice(["rock", "paper", "scissors"])
    # If the computer chooses rock
    if computer == "rock":
        # The computer wins
        print("Computer chose rock. You lose!")
    # If the computer chooses paper
    elif computer == "paper":
        # The user wins
        print("Computer chose paper. You win!")
    # If the computer chooses scissors
    else:
        # The game is a draw
        print("Computer chose scissors. It's a draw!")

# The function that will be called when the user chooses to quit
def quit():
    # The program ends
    exit()

# The function that will be called when the user enters an invalid option
def invalid():
    # An error message is displayed
    print("Invalid option!")


# The main function
def main():
    while True:
        # The user is asked to choose an option
        choice = input("Choose rock, paper, scissors or quit: ")
        # If the user chooses rock
        if choice == "rock":
            # The rock function is called
            rock()
        # If the user chooses paper
        elif choice == "paper":
            # The paper function is called
            paper()
        # If the user chooses scissors
        elif choice == "scissors":
            # The scissors function is called
            scissors()
        # If the user chooses to quit
        elif choice == "quit":
            # The quit function is called
            quit()
        # If the user enters an invalid option
        else:
            # The invalid function is called
            invalid()

# The main function is called
main()
