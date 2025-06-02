#Typecast - the process of converting  a variable from one type to another
# we've the functions str(), int(), float(), and bool() to help in conversations.

name = "Mike Kipruto"
age = 29
gpa = 3.2
is_student = True

#checking types

print(type(name))
print(type(age))
print(type(age))
print(type(gpa))
print(type(is_student))

# converting the gpa float to an integer
gpa = int(gpa)
print(gpa)
print(type(gpa))

# converting the age integer to a float
age = float(age)
print(age)
print(type(age))

# converting the age integer to a string
age = str(age)
print(age)
print(type(age))

# converting the name string to a boolean, for this, if the String is empty it returns a false, and a true if there is any value
name = bool(name)
print(name)
print(type(name))

# converting the is_student boolean to a string
is_student = str(is_student)
print(is_student)
print(type(is_student))