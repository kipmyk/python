# Python weight conversion program

weight = float(input("Enter your weight: "))
unit = input("Is this weight in Kilograms or Pounds (K or L): ")

if unit == "K":
    weight = weight * 2.205 # converting to Pounds
    unit = "Lbs."
    print(f"Your weight is {round(weight, 1)} {unit} ")
elif unit == "L":
    weight = weight / 2.205  # converting to Kilograms
    unit = "Kgs."
    print(f"Your weight is {round(weight, 1)} {unit} ")
else:
    print(f"{unit} was not valid!")