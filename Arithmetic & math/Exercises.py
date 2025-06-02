# Exercise 1: Calculate the area and the circumference of a circle
import math

pi = math.pi  # π = 3.14159...

radius = float(input("What is the radius of the circle?: "))

# Area of a circle: π * r² using math.pow()

area = pi * pow(radius, 2)

# Circumference of a circle: 2 * π * r
circumference = 2 * pi * radius

# Output
print(f"The Area of the circle is: {round(area,2)}cm²")
print(f"Circumference of the circle is: {round(circumference,2)} cm")

# Exercise 2: Calculate the Hypotenuse of a triangle
# Formula of Hypotenuse = √(a² + b². This calculates the hypotenuse of a right-angled triangle using the Pythagorean theorem

import math

# Input: lengths of the two shorter sides
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))

# Calculate hypotenuse using math.sqrt() and pow()
hypotenuse = math.sqrt(pow(a, 2) + pow(b, 2))

# Output the result
print(f"The Hypotenuse of a right-angled triangle using the Pythagorean theorem is: {round(hypotenuse,2)}")


