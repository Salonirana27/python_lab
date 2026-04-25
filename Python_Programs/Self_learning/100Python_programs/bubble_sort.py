# Program to sort list using bubble sort

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

for i in range(n):
    for j in range(0, n - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print("Sorted List:", lst)

# Output:
# Enter number of elements: 4
# 5 2 8 1
# Sorted List: [1, 2, 5, 8]