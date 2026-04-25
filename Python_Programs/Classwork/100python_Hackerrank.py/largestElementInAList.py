#Find largest element in a list.


def find_largest(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

# Taking input
numbers = list(map(int, input("Enter space-separated numbers: ").split()))

# Printing result
print("Largest element is:", find_largest(numbers))

# output
""" Enter space-separated numbers: 10 45 23 89 12
Largest element is: 89"""