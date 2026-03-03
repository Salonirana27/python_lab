# Program to check if two lists are equal

list1 = list(map(int, input("Enter first list elements: ").split()))
list2 = list(map(int, input("Enter second list elements: ").split()))

if list1 == list2:
    print("Lists are equal")
else:
    print("Lists are not equal")

# Output:
# Enter first list elements: 1 2 3
# Enter second list elements: 1 2 3
# Lists are equal