# Program to perform Linear Search

lst = list(map(int, input("Enter elements: ").split()))
key = int(input("Enter element to search: "))

found = False

for i in range(len(lst)):
    if lst[i] == key:
        print("Element found at index", i)
        found = True
        break

if not found:
    print("Element not found")

# Output:
# Enter elements: 2 5 7 9
# Enter element to search: 7
# Element found at index 2