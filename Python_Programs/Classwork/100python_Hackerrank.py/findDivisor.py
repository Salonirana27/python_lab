#find all divisor of a number

n = int(input("enter number: "))

# Print divisors
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
        
        #output
        """enter number: 42
1
2
3
6
7
14
21
42"""