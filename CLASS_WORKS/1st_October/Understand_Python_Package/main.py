from mypackage import mathutils
from mypackage import cube


# using custom package
num = int(input("Enter a Number: "))

print(f"Square of {num}: {mathutils.square(num)}")
print(f"Cube of {num}: {mathutils.cube(num)}")

print(cube(num))

