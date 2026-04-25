# Problem Statement: Generate Fibonacci series using function.

def fibonacci(n):
    series = []
    a, b = 0, 1
    for i in range(n):
        series.append(str(a))
        a, b = b, a + b
    return " ".join(series)

num = int(input("enter number: "))
print(fibonacci(num))

#output
"""enter number: 10
0 1 1 2 3 5 8 13 21 34"""

