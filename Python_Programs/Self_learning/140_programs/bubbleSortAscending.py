# Program to sort list using Bubble Sort (Ascending)

n = int(input("Enter number of elements: "))
lst = list(map(int, input("Enter elements: ").split()))

for i in range(n):
    for j in range(0, n - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print("Sorted List (Ascending):", lst)

# Output:
# Enter number of elements: 5
# Enter elements: 5 3 8 1 2
# Sorted List (Ascending): [1, 2, 3, 5, 8]