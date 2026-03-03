# Program to perform Binary Search

lst = list(map(int, input("Enter sorted elements: ").split()))
key = int(input("Enter element to search: "))

low = 0
high = len(lst) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if lst[mid] == key:
        print("Element found at index", mid)
        found = True
        break
    elif lst[mid] < key:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found")

# Output:
# Enter sorted elements: 1 3 5 7 9
# Enter element to search: 5
# Element found at index 2