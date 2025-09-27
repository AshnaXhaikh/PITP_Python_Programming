"""generates a random number between 1 and 100. The user has to guess the number.
    The program should give a feedback on whether the guess is too high or too low.
    The game ends when the user guesses the correct number."""

import random
secret_number = random.randint(1, 100)
while True: 
    guess = int(input("Guess the number between 1 and 100: "))
    if guess == secret_number: 
        print("Congratulations! you have guessed the correct number.")
        break
    elif guess < secret_number: 
        print("Too low! Try again.")
    else:
        print("Too High! Try again.")
