while True:
    unit = input("Is this temperature in Celsius or Fahrenheit (C/F)?: ").upper()
    if unit in ("C", "F"):
        break
    print(f"Invalid {unit} is an invalid unit of measurement. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = (temp * 9/5) + 32
    unit = "°F"
elif unit == "F":
    temp = (temp - 32) * 5/9
    unit = "°C"

print(f"The current temperature is {round(temp, 2)} {unit}")