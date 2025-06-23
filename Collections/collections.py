# collection = single "variable" used to store multiple values
# List = [] ordered and changeable. Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

#List

fruits = ['apple','orange','banana', 'coconut']

#print(fruits[:3])

# for fruit in fruits:
#     print(fruit)

fruits.append("Honey")

for fruit in fruits:
    print(fruit)

# print(dir(fruits))

from collections import namedtuple

Person = namedtuple('Person', ['name', 'age'])
p = Person(name='Alice', age=30)

print(p.name)  # Alice
print(p.age)   # 30
