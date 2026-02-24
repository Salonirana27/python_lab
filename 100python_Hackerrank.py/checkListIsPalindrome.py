# Problem Statement: Check whether list is palindrome.

def is_palindrome(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        if lst[left] != lst[right]:
            return False
        left += 1
        right -= 1
    return True

# Taking input
numbers = list(map(int, input("Enter list elements: ").split()))

# Printing result
if is_palindrome(numbers):
    print("List is Palindrome")
else:
    print("List is Not Palindrome")

# output
""" Enter list elements: 1 2 3 2 1
List is Palindrome """