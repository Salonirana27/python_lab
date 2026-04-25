#Convert tuple to list.


def tuple_to_list(tpl):
    return list(tpl)

# Taking input
numbers = tuple(map(int, input("Enter tuple elements: ").split()))

# Converting and printing result
converted_list = tuple_to_list(numbers)
print("Converted list is:", converted_list)

# output
# Enter tuple elements: 1 2 3 4 5
 # Converted list is: [1, 2, 3, 4, 5] 