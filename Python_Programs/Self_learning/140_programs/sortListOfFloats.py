# Program to sort float numbers

numbers = list(map(float, input("Enter float numbers: ").split()))

numbers.sort()

print("Sorted Float List:", numbers)

# Output:
# Enter float numbers: 3.2 1.5 2.8
# Sorted Float List: [1.5, 2.8, 3.2]