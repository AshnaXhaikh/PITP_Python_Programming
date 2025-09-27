"""take input number from the user"""
total = 0
while True:
    num = int(input("Enter a number: "))
    if num > 100:
        break
    total += num
print("The total Sum = ", total)
