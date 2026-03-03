# Program to filter even numbers using lambda

n = int(input("Enter number of elements: "))
numbers = []

for i in range(n):
    numbers.append(int(input("Enter element: ")))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print("Even numbers:", even_numbers)

# Output:
# Enter number of elements: 5
# 1 2 3 4 5
# Even numbers: [2, 4]