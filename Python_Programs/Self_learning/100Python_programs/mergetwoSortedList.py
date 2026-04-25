# Program to merge two sorted lists

list1 = list(map(int, input("Enter first sorted list: ").split()))
list2 = list(map(int, input("Enter second sorted list: ").split()))

merged = sorted(list1 + list2)

print("Merged Sorted List:", merged)

# Output:
# Enter first sorted list: 1 3 5
# Enter second sorted list: 2 4 6
# Merged Sorted List: [1, 2, 3, 4, 5, 6]