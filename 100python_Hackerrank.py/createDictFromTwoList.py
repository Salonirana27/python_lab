# Program to create dictionary from two lists

keys = ["a", "b", "c"]
values = [1, 2, 3]

data = {}

for i in range(len(keys)):
    data[keys[i]] = values[i]

print("Created dictionary:", data)
#Output:

#Created dictionary: {'a': 1, 'b': 2, 'c': 3}