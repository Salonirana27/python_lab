# Program to check if tuple contains a value

elements = tuple(input("Enter tuple elements: ").split())
value = input("Enter value to search: ")

if value in elements:
    print("Value Found in Tuple")
else:
    print("Value Not Found")

# Output:
# Enter tuple elements: 10 20 30
# Enter value to search: 20
# Value Found in Tuple