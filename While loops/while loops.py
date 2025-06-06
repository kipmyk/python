# While loop will execute some code while a condition remains true

name = input("What is your name?: ")

while name == "":
    print("Please enter your name")
    name = input("What is your name?: ")  # Ask again if input is empty

print(f"Hello, {name}")
