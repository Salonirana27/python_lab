# Problem Statement: Find common elements between two lists.

def find_common(list1, list2):
    common = []
    for num in list1:
        if num in list2 and num not in common:
            common.append(num)
    return common

# Taking input
list1 = list(map(int, input("Enter first list elements: ").split()))
list2 = list(map(int, input("Enter second list elements: ").split()))

# Printing result
result = find_common(list1, list2)
print("Common elements are:", *result)

#output
""" Enter first list elements: 1 2 3 4 5
Enter second list elements: 3 4 5 6 7
 Common elements are: 3 4 5 """