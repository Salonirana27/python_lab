# Program to sort list based on user choice

numbers = list(map(int, input("Enter numbers: ").split()))
choice = input("Enter 'A' for Ascending or 'D' for Descending: ")

if choice.upper() == 'A':
    numbers.sort()
elif choice.upper() == 'D':
    numbers.sort(reverse=True)
else:
    print("Invalid Choice")

print("Sorted List:", numbers)

# Output:
# Enter numbers: 4 9 1
# Enter 'A' for Ascending or 'D' for Descending: D
# Sorted List: [9, 4, 1]