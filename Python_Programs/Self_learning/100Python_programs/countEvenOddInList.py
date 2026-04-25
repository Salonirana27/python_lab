# Program to count even and odd numbers

lst = list(map(int, input("Enter elements: ").split()))

even = odd = 0

for num in lst:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even count:", even)
print("Odd count:", odd)

# Output:
# Enter elements: 1 2 3 4 5
# Even count: 2
# Odd count: 3