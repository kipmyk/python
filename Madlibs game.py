# Madlibs game
# Word game where you create a story by filling in the blanks with some random words

# variable of our game story
last_visit = input("When was your last visit?: ")
country = input ("Which country did you visit last?: ")
city = input("Which city did you?: ")
park = input("Which National park did you visit while in that country?: ")
animal_seen = input("Which animal did you see?: ")

print(f"{last_visit}, I went to {park} Park, in {city}, {country}.")
print(f"While in {park}, I saw a {animal_seen}")