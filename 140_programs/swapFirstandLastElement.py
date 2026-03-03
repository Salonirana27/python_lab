# Program to swap first and last element of a list

lst = list(map(int, input("Enter list elements: ").split()))

# Swapping
lst[0], lst[-1] = lst[-1], lst[0]

print("Updated List:", lst)

# Output:
# Enter list elements: 10 20 30 40
# Updated List: [40, 20, 30, 10]