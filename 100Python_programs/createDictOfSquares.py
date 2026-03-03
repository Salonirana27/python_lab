# Program to create dictionary of squares

n = int(input("Enter limit: "))

squares = {}

for i in range(1, n + 1):
    squares[i] = i * i

print("Dictionary of squares:", squares)

# Output:
# Enter limit: 5
# Dictionary of squares: {1:1, 2:4, 3:9, 4:16, 5:25}