
# Additional(+) operator
operator_type = "Additional(+) operator"
followers = 0
# followers = followers + 1 # This approach is the Standard assignment with addition
followers +=1 # This approach is the Augmented assignment operator (addition)
print(f"{operator_type} results is: {followers}")

# Substraction(-) operator
operator_type = "Substraction(-) operator"
followers = 10
# followers = followers 2. This approach is the Standard assignment
followers -= 2 # This approach is the Augmented assignment operator Substraction(-)
print(f"{operator_type} results is: {followers}")

# Multiplication (*) operator
operator_type = "Multiplication (*) operator"
followers = 15
# followers = followers * 2. This approach is the Standard assignment
followers *=2  # This approach is the Augmented assignment operator
print(f"{operator_type} results is: {followers}")

# Division (/) operator
operator_type = "Division (/) operator"
followers = 32
# followers = followers / 2. This approach is the Standard assignment
followers /=2  # This approach is the Augmented assignment operator
print(f"{operator_type} results is: {followers}")

# Exponents (**) operator
operator_type = "Exponents (**) operator"
followers = 2
# followers = followers ** 2. This approach is the Standard assignment
followers **=2  # This approach is the Augmented assignment operator
print(f"{operator_type} results is: {followers}")

# Modulus (%) operator - this gives you the remainder of any division
operator_type = "Modulus (%) operator"
followers = 1205
followers_remainder = followers % 2
print(f"{operator_type} results is: {followers_remainder}")