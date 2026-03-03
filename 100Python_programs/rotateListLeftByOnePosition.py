# Program to rotate list left by one position

lst = list(map(int, input("Enter elements: ").split()))

rotated = lst[1:] + [lst[0]]

print("Rotated List:", rotated)

# Output:
# Enter elements: 1 2 3 4
# Rotated List: [2, 3, 4, 1]