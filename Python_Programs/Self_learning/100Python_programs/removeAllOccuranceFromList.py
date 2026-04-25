# Program to remove all occurrences of a given element

n = int(input("Enter number of elements: "))
lst = list(map(int, input("Enter elements: ").split()))

key = int(input("Enter element to remove: "))

result = [x for x in lst if x != key]

print("Updated List:", result)

# Output:
# Enter number of elements: 5
# Enter elements: 1 2 2 3 4
# Enter element to remove: 2
# Updated List: [1, 3, 4]