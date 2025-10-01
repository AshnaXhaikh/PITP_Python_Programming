"""Program to use custom module."""
import mymodule

Hello = mymodule.greet("Ashna")
print(Hello)

Sum = mymodule.add(23, 21)
print(f"Sum = {Sum}")



# Guess Number Game
mymodule.guess_num_game()

