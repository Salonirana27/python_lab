# Program to find length of list without len()

lst = input("Enter elements separated by space: ").split()

count = 0
for _ in lst:
    count += 1

print("Length of List:", count)

# Output:
# Enter elements separated by space: 1 2 3 4
# Length of List: 4