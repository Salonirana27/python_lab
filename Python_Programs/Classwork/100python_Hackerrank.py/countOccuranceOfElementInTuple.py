#  Count occurrence of element in tuple.


def count_occurrence(tpl, element):
    count = 0
    for num in tpl:
        if num == element:
            count += 1
    return count

# Taking input
numbers = tuple(map(int, input("Enter tuple elements: ").split()))
element = int(input("Enter element to count: "))

# Printing result
print("Occurrence is:", count_occurrence(numbers, element))

# output
# Enter tuple elements: 1 2 3 2 4 2 5
# Enter element to count: 2
# Occurrence is: 3