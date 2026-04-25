# Program using map function to convert strings to integers

numbers = input("Enter numbers: ").split()

converted = list(map(int, numbers))

print("Converted List:", converted)

# Output:
# Enter numbers: 1 2 3 4
# Converted List: [1, 2, 3, 4]