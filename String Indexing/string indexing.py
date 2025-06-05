# String Indexing Python

# It allows use to access elements of sequence using [] (indexing operator) [Start : End : Step]

# Python uses zero-based indexing, so the first character has index 0, the second 1, and so on.

text = "Python"
print(text[0])  # P
print(text[1])  # y

credit_card_number = "1234-5678-9012-3556"

print((credit_card_number[0]))

print((credit_card_number[0:4]))
print((credit_card_number[5:9]))
print(credit_card_number[5:])

print(credit_card_number[-1]) # negative index

# using step
print(credit_card_number[::2])