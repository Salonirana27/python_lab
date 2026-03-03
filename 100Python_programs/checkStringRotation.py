# Program to find maximum difference (larger after smaller)

lst = list(map(int, input("Enter elements: ").split()))

min_value = lst[0]
max_diff = 0

for i in range(1, len(lst)):
    if lst[i] - min_value > max_diff:
        max_diff = lst[i] - min_value
    if lst[i] < min_value:
        min_value = lst[i]

print("Maximum Difference:", max_diff)

# Output:
# Enter elements: 2 3 10 6 4 8 1
# Maximum Difference: 8