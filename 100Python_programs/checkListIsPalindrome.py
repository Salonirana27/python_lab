# Program to check if list is palindrome

lst = input("Enter elements: ").split()

if lst == lst[::-1]:
    print("List is Palindrome")
else:
    print("List is Not Palindrome")

#  Output:
# Enter elements: 1 2 3 2 1
# List is Palindrome