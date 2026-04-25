# Program to sort list in descending order

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

numbers.sort(reverse=True)

print("Sorted List (Descending):", numbers)

#  Output:
# Enter numbers separated by space: 5 2 8 1
# Sorted List (Descending): [8, 5, 2, 1]