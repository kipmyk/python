
# Exercise 1:
# Prompt the user for their age and ensure it's a non-negative number.
# Then display the age with the correct singular/plural form for "year(s)".
# Use conditional expression ('s' if age != 1 else '') to handle singular/plural for "year(s)".


age = int(input("What is your age?: "))

while age < 0:
    print("Age can't be a negative")
    age = int(input("What is your age?: "))

print(f"You are {age} year{'s' if age > 2 else ''} old")

# Exercise 2:

food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another food you like (q to quit): ")

print("bye")

# Exercise 3: - adding logical operators to the while loop

num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid!")
    num = int(input("Enter a number between 1 - 10: "))

print(f"Your number is {num}")

# Exercise 4: Python compound interest calculator

# Get valid principle amount
principle = 0
while principle <= 0:
    try:
        principle = float(input("Enter the principal amount: "))
        if principle <= 0:
            print("Principal can't be less than or equal to zero")
    except ValueError:
        print("Please enter a valid number")

# Get valid rate
rate = 0
while rate <= 0:
    try:
        rate = float(input("Enter the annual interest rate (in %): "))
        if rate <= 0:
            print("Rate can't be less than or equal to zero")
    except ValueError:
        print("Please enter a valid number")

# Get valid time in years
time = 0
while time <= 0:
    try:
        time = float(input("Enter the time in years: "))
        if time <= 0:
            print("Time can't be less than or equal to zero")
    except ValueError:
        print("Please enter a valid number")

# Compound Interest Formula: A = P * (1 + r/100) ** t
amount = principle * (1 + rate / 100) ** time
interest = amount - principle

# Output results
print(f"\nPrincipal: ksh.{principle:.2f}")
print(f"Rate: {rate:.2f}%")
print(f"Time: {time} years")
print(f"Compound Interest: ksh.{interest:.2f}")
print(f"Total Amount: ksh.{amount:.2f}")
