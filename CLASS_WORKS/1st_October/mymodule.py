"""This is my custom module where I'll keep my reusable functions.
Inside mymodule.py, let's define the function guess_num_game()."""

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b




def guess_num_game():
    import random
    # python guessing number function
    secret = random.randint(1, 100)
    
    print("I am thinking of a number between 1 to 100")
    
    while True:
        guess = int(input("Enter your guess(0 to quit): "))
        print(f"You entered: {guess}")

        if guess == 0:
            print("Exit the game.")
            break

        elif guess == secret:
            print(f"Congrats! you've guessed the exact number.")
            break

        elif guess > secret:
            print(f"Too High!, Try again.")

        else:
            print(f"Too Low!, Try agian.")