# Program to find smallest element in a list

lst = list(map(int, input("Enter elements: ").split()))

smallest = lst[0]

for num in lst:
    if num < smallest:
        smallest = num

print("Smallest Element:", smallest)

# Output:
# Enter elements: 10 5 8 2 7
# Smallest Element: 2