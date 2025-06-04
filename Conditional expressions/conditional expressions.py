
# Print or assign one of two values based on one condition
# X if condition else y
# Python has a conditional expression (sometimes called a "ternary operator").
# You can write operations like if statements in one line with conditional expressions.

a = 1

if a % 2 == 0:
    print('even')
else:
    print('odd')
# odd

num = 5

print("Positive" if num > 0 else "Negative")

result = "EVEN" if num % 2 == 0 else "ODD"
print(result)

user_role = "admin"

access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)

a = 1
result = a * 10 if a % 2 == 0 else a * 100
print(result)
# 100

a = 2
result = a * 10 if a % 2 == 0 else a * 100
print(result)
# 20