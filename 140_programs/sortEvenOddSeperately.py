# Program to sort even and odd numbers separately

lst = list(map(int, input("Enter elements: ").split()))

even = sorted([x for x in lst if x % 2 == 0])
odd = sorted([x for x in lst if x % 2 != 0])

print("Even Numbers Sorted:", even)
print("Odd Numbers Sorted:", odd)

# Output:
# Enter elements: 5 2 9 4 7
# Even Numbers Sorted: [2, 4]
# Odd Numbers Sorted: [5, 7, 9]