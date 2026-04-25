# Program to sort elements of a set

numbers = set(map(int, input("Enter numbers: ").split()))

sorted_list = sorted(numbers)

print("Sorted Set Elements:", sorted_list)

#  Output:
# Enter numbers: 4 2 5 2 1
# Sorted Set Elements: [1, 2, 4, 5]