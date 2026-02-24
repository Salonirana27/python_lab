#  Sort dictionary by values.


def sort_dict_by_values(d):
    sorted_dict = {}
    sorted_items = sorted(d.items(), key=lambda item: item[1])
    for key, value in sorted_items:
        sorted_dict[key] = value
    return sorted_dict

# Taking input
n = int(input("Enter number of elements: "))
data = {}

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    data[key] = value

# Sorting dictionary
result = sort_dict_by_values(data)

# Printing result
print("Dictionary sorted by values:", result)

# output
# Enter number of elements: 3
# Enter key: a
# Enter value: 30
# Enter key: b
# Enter value: 10
# Enter key: c
# Enter value: 20
# Dictionary sorted by values: {'b': 10, 'c': 20, 'a': 30}