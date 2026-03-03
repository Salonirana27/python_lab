# Program to create tuple from user input

elements = input("Enter elements separated by space: ").split()

tuple_data = tuple(elements)

print("Created Tuple:", tuple_data)

# Output:
# Enter elements separated by space: 10 20 30
# Created Tuple: ('10', '20', '30')