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