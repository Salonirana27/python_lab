# Program to merge two lists and sort

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

merged = list1 + list2
merged.sort()

print("Merged and Sorted List:", merged)

# Output:
# Enter first list: 1 3 5
# Enter second list: 2 4 6
# Merged and Sorted List: [1, 2, 3, 4, 5, 6]