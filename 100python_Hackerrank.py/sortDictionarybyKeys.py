#  Sort dictionary by keys.


def sort_dict_by_keys(d):
    sorted_dict = {}
    for key in sorted(d):
        sorted_dict[key] = d[key]
    return sorted_dict

# Taking input
n = int(input("Enter number of elements: "))
data = {}

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data[key] = value

# Sorting dictionary
result = sort_dict_by_keys(data)

# Printing result
print("Dictionary sorted by keys:", result)

#output
# Enter number of elements: 3
# Enter key: b
# Enter value: 20
# Enter key: a
# Enter value: 10
# Enter key: c
# Enter value: 30
# Dictionary sorted by keys: {'a': '10', 'b': '20', 'c': '30'}