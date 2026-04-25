# Program using lambda function to find cube

num = int(input("Enter a number: "))

cube = lambda x: x ** 3

print("Cube:", cube(num))

# Output:
# Enter a number: 4
# Cube: 64