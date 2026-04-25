# Program to find sum of all dictionary values

data = {"a": 10, "b": 20, "c": 30}

total = 0

for key in data:
    total = total + data[key]

print("Sum of values =", total)
#Output:


#Sum of values = 60