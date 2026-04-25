#Sort a list without using sort method.


def sort_list(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

# Taking input
numbers = list(map(int, input("Enter space-separated numbers: ").split()))

# Printing result
sorted_list = sort_list(numbers)
print(*sorted_list)

#output
"""Enter space-separated numbers: 5 2 9 1 3
 1 2 3 5 9"""