# Program to find sum of elements at even index

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input("Enter element: ")))

sum_even_index = 0

for i in range(0, n, 2):
    sum_even_index += lst[i]

print("Sum of elements at even index:", sum_even_index)

# Output:
# Enter number of elements: 5
# 10 20 30 40 50
# Sum of elements at even index: 90