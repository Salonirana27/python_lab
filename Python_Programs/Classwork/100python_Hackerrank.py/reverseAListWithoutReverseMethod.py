# Problem Statement: Reverse a list without reverse method.


def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

# Taking input
numbers = list(map(int, input("Enter space-separated numbers: ").split()))

# Printing result
result = reverse_list(numbers)
print(*result)

# output
""" Enter space-separated numbers: 1 2 3 4 5
 5 4 3 2 1 """