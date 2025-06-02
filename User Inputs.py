# Input() = A function that prompts the user to enter data.
# It returns the entered data as a string

name = input("What is your name?: ")
age = int(input ("How old are you? "))
age = age + 1
print(f"Hello {name}")
print("HAPPY BIRTHDAY!!!")
print(f"You are {age} years old")

# Exercise 1: Calculate the Area of a Rectangle
#inputs
length = float(input("What is the Length?: "))
width = float(input("What is the width?: "))
area = length * width

print(f"The Area of the Rectangle is {area} cm²")

# Exercise 2: Creating a shopping cart program
item = input("What would you like to purchase?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity
print (f"You have bought {quantity} X {item}/s")
print(f"Your total is: ${total}")