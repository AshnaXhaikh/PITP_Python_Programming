"""Build a Calculator"""
a = int(input("Enter a num: "))
b = int(input("Enter another num: "))

operation = int(input("Enter (1, 2, 3, 4) an operation (Addition, Subtraction, Division, Multiplication): "))

if operation ==1:
    print(a + b)
elif operation == 2:
    print(a-b)
elif operation == 3:
    print(a/b)
elif operation == 4:
    print(a*b)
else:
    print("Please choose an one from the given operations.")
