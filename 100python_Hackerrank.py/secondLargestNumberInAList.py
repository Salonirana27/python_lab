#Find second largest number in list.


def second_largest(lst):
    largest = second = float('-inf')
    
    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    
    return second

# Taking input
numbers = list(map(int, input("Enter space-separated numbers: ").split()))

# Printing result
print(second_largest(numbers))

#output
""" Enter space-separated numbers: 10 45 23 89 12
 4 5 """