# Program to sort list using Selection Sort

n = int(input("Enter number of elements: "))
lst = list(map(int, input("Enter elements: ").split()))

for i in range(n):
    min_index = i
    for j in range(i + 1, n):
        if lst[j] < lst[min_index]:
            min_index = j
    lst[i], lst[min_index] = lst[min_index], lst[i]

print("Sorted List:", lst)

#  Output:
# Enter number of elements: 4
# Enter elements: 9 4 6 2
# Sorted List: [2, 4, 6, 9]