# Logical operators = they allow one to evaluate multiple conditions such as (Or, and, Not)

# or
# Returns True if at least one of the conditions is True.
# Only returns False if both conditions are False.

temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled!")

# and
# Returns True only if both conditions are True.
# If one or both are False, the result is False.

temp = 36
is_sunny = True

if temp >= 35 and is_sunny:
    print("It is HOT outside 🥵")
    print("It is SUNNY ☀️")
elif temp <= 0 and is_sunny:
    print("It is COLD outside 🥶")
    print("It is SUNNY ☀️")
elif 28 > temp > 0 and is_sunny:
    print("It is warm outside 🌤️")
    print("It is SUNNY ☀️")


# not
# Reverses the condition.
# If the condition is True, it becomes False.
# If the condition is False, it becomes True.
# Not logical operator - it inverts the condition (Not False, Not True)

temp = float(input("What is the temperature outside?: "))
is_sunny = False

if temp >= 35 and is_sunny:
    print("It is HOT outside 🥵")
    print("It is SUNNY ☀️")
elif temp <= 0 and not is_sunny:
    print("It is COLD outside 🥶")
    print("It is cloudy ⛅️️")
elif 28 > temp > 0 and not is_sunny:
    print("It is warm outside 🌤️")
    print("It is cloudy ⛅️️")


