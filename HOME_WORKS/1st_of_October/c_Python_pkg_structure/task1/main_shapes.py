# This file imports the function directly from the module inside the package.
from shapes.circle import area

# use the imported function
radius = 5
circle_area = area(radius)

print(f"using the 'shapes' package:")
print(f"Radius of circle: {radius}")
print(f"Area of circle: {circle_area:.2f}")