# Program to sort list using sorted() function

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

sorted_list = sorted(numbers)

print("Original List:", numbers)
print("Sorted List:", sorted_list)

# Output:
# Enter numbers separated by space: 4 7 1 9
# Original List: [4, 7, 1, 9]
# Sorted List: [1, 4, 7, 9]