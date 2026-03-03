# Program to find union and intersection

list1 = list(map(int, input("Enter first list: ").split()))
list2 = list(map(int, input("Enter second list: ").split()))

union = list(set(list1) | set(list2))
intersection = list(set(list1) & set(list2))

print("Union:", union)
print("Intersection:", intersection)

# Output:
# Enter first list: 1 2 3
# Enter second list: 2 3 4
# Union: [1, 2, 3, 4]
# Intersection: [2, 3]