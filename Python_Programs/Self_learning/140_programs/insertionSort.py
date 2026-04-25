# Program to sort list using Insertion Sort

n = int(input("Enter number of elements: "))
lst = list(map(int, input("Enter elements: ").split()))

for i in range(1, n):
    key = lst[i]
    j = i - 1
    while j >= 0 and lst[j] > key:
        lst[j + 1] = lst[j]
        j -= 1
    lst[j + 1] = key

print("Sorted List:", lst)

#  Output:
# Enter number of elements: 4
# Enter elements: 5 2 9 1
# Sorted List: [1, 2, 5, 9]