# Program to sort list using Bubble Sort (Descending)

n = int(input("Enter number of elements: "))
lst = list(map(int, input("Enter elements: ").split()))

for i in range(n):
    for j in range(0, n - i - 1):
        if lst[j] < lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print("Sorted List (Descending):", lst)

# Output:
# Enter number of elements: 4
# Enter elements: 2 7 1 5
# Sorted List (Descending): [7, 5, 2, 1]