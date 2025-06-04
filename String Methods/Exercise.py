# Validate user input exercise
# 1. The username is no more than 12 characters
# 2. The username must not contain spaces
# 3. The username must not contain digits

username = input("Please enter your username: ")

if len(username) > 12:
    print("The username should not be more than 12 characters long.")
elif not username.find(" ") == -1:
    print("The username should not contain spaces.")
elif any(char.isdigit() for char in username):
    print("The username should not contain digits.")
else:
    print(f"Welcome {username.capitalize()}.")
