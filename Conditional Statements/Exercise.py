# Exercise 1:
from conditional import for_sale

response = input("Are you interested in learning Python (Y/N)?: ")

if response == "Y":
    print("You can use this repo for free!")
else:
    print("Then you can browser, and learn math!")

# Exercise 2:
name = input("Enter your name: ")

if name == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name}")

# Exercise 3:

for_sale = True

if for_sale:
    print("This item is for sale!")
else:
    print("This item is not for sale!")