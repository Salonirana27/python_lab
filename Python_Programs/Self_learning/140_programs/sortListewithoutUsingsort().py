# Program to sort list without using built-in functions

lst = list(map(int, input("Enter elements: ").split()))

sorted_list = []

while lst:
    smallest = min(lst)
    sorted_list.append(smallest)
    lst.remove(smallest)

print("Sorted List:", sorted_list)

# Output:
# Enter elements: 7 2 5 1
# Sorted List: [1, 2, 5, 7]