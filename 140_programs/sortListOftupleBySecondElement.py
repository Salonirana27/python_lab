# Program to sort list of tuples by second element

lst = [(1, 3), (2, 1), (4, 2)]

sorted_list = sorted(lst, key=lambda x: x[1])

print("Sorted List:", sorted_list)

#  Output:
# Sorted List: [(2, 1), (4, 2), (1, 3)]