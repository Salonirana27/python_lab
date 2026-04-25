# Program to find key with maximum value

data = {"A": 45, "B": 78, "C": 60}

max_key = ""
max_value = 0

for key in data:
    if data[key] > max_value:
        max_value = data[key]
        max_key = key

print("Key with maximum value:", max_key)
print("Value:", max_value)


#Output:
#Key with maximum value: B
#Value: 78