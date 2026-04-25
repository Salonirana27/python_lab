# Program to check if list is sorted

lst = list(map(int, input("Enter elements: ").split()))

if lst == sorted(lst):
    print("List is Sorted")
else:
    print("List is Not Sorted")

#  Output:
# Enter elements: 1 2 3 4
# List is Sorted