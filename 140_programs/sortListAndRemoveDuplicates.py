# Program to sort list and remove duplicates

numbers = list(map(int, input("Enter numbers: ").split()))

unique_sorted = sorted(set(numbers))

print("Sorted Unique List:", unique_sorted)

# Output:
# Enter numbers: 4 2 2 1 4
# Sorted Unique List: [1, 2, 4]