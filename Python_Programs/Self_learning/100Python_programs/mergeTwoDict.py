# Program to merge two dictionaries

dict1 = eval(input("Enter first dictionary: "))
dict2 = eval(input("Enter second dictionary: "))

merged = dict1.copy()
merged.update(dict2)

print("Merged Dictionary:", merged)

# Output:
# Enter first dictionary: {1:10, 2:20}
# Enter second dictionary: {3:30}
# Merged Dictionary: {1:10, 2:20, 3:30}