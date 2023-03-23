# Guess the Number - The computer will choose a random number, and players must take turns guessing the number.

import random

# Generate a random number between 1 and 10
secret_num = random.randint(1, 10)
guesses = []

# Limit the number of guesses
while len(guesses) < 5:
    try:
        # Get a number guess from the player
        guess = int(input("Guess a number between 1 and 10: "))
    except ValueError:
        print("{} isn't a number!".format(guess))
    else:
        # Compare guess to secret number
        if guess == secret_num:
            print("You got it! My number was {}".format(secret_num))
            break
        elif guess < secret_num:
            print("My number is higher than {}".format(guess))
        else:
            print("My number is lower than {}".format(guess))
        guesses.append(guess)

else:
    print("You didn't get it! My number was {}".format(secret_num))

# Print what the player guessed
print("You guessed {} times".format(len(guesses)))
print("You guessed these numbers: ")
for guess in guesses:
    print(guess)
