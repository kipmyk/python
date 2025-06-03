# Python calculator

operator = input("Enter an operator (+ - * /): ")

numb1 = float(input("Enter the first number: "))
numb2 = float(input("Enter the second number: "))

if operator == "+":
    sum = numb1 + numb2
    print(f"The sum of the two numbers is: {round(sum)}")
elif operator == "-":
    diff = numb1 - numb2
    print(f"The difference of the two numbers is: {round(diff)}")
elif operator == "*":
    multiplication = numb1 * numb2
    print(f"The multiplication of the two numbers is: {round(multiplication)}")
elif operator == "/":
    division = numb1/numb2
    print(f"The division of the two numbers is: {round(division)}")
else:
    print(f"The {operator} is not a valid operator!")