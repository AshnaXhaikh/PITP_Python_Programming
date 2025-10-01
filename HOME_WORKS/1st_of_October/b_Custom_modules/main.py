"""Import calculator and greetings modules."""

import calculator
import greetings

# Using functions from greeting module
greet_msg = greetings.say_hello("Ashna")
print(greet_msg)

# Using function from calculator module
result = calculator.multiply(5, 9)
print(f"Multiplication Result: {result}")

result_add = calculator.add(12, 238)
print(f"Addition Result: {result_add}")