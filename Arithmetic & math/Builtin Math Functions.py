x = 3.14
y = -8
z = 10

# round() function - Rounds a floating-point number to the nearest whole number
function_type = "Round() function"
results = round(x)
print(f"{function_type} results is: {results}")

# abs() function - Returns the absolute (non-negative) value of a number
function_type = "Abs() function"
results = abs(y)
print(f"{function_type} results is: {results}")

# pow() function - Raises the first number to the power of the second (z^x)
function_type = "Power() function"
results = pow(z, x)
print(f"{function_type} results is: {results}")

# max() function - Returns the largest value among the given numbers
function_type = "Max() function"
results = max(x, y, z)
print(f"{function_type} results is: {results}")

# min() function - Returns the smallest value among the given numbers
function_type = "Min() function"
results = min(x, y, z)
print(f"{function_type} results is: {results}")

# sum() function - Returns the total sum of all values in an iterable
function_type = "Sum() function"
results = sum([x, y, z])
print(f"{function_type} results is: {results}")

# divmod() function - Returns a tuple with quotient and remainder of division
function_type = "Divmod() function"
results = divmod(z, 3)
print(f"{function_type} results is: {results}")
