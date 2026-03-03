# Program to create dictionary using two lists

keys = input("Enter keys: ").split()
values = input("Enter values: ").split()

dictionary = {}

for i in range(len(keys)):
    dictionary[keys[i]] = values[i]

print("Created Dictionary:", dictionary)

# Output:
# Enter keys: a b c
# Enter values: 1 2 3
# Created Dictionary: {'a':'1', 'b':'2', 'c':'3'}