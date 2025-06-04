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