# or
# Returns True if at least one of the conditions is True.
# Only returns False if both conditions are False.

temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled!")