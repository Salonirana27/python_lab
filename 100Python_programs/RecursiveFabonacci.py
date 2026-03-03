# Program to generate Fibonacci using recursion

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter number of terms: "))

print("Fibonacci Series:")
for i in range(n):
    print(fibonacci(i), end=" ")

# Output:
# Enter number of terms: 5
# Fibonacci Series:
# 0 1 1 2 3