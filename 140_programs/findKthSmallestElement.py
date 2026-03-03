# Program to find k-th smallest element

lst = list(map(int, input("Enter elements: ").split()))
k = int(input("Enter value of k: "))

lst.sort()

print(f"{k}th Smallest Element:", lst[k-1])

#  Output:
# Enter elements: 7 2 9 1
# Enter value of k: 2
# 2th Smallest Element: 2