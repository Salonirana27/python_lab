#Merge two lists and remove duplicates.


def merge_and_remove_duplicates(list1, list2):
    merged = list1 + list2
    unique = []
    for num in merged:
        if num not in unique:
            unique.append(num)
    return unique

# Taking input
list1 = list(map(int, input("Enter first list elements: ").split()))
list2 = list(map(int, input("Enter second list elements: ").split()))

# Printing result
result = merge_and_remove_duplicates(list1, list2)
print(*result)

#output
""" Enter first list elements: 1 2 3 4
Enter second list elements: 3 4 5 6
1 2 3 4 5 6"""