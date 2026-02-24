# generate fibonacci series using for loop 

n = int(input("enter number: "))

a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
    
    #output
    """enter number: 12
0 1 1 2 3 5 8 13 21 34 55 89 """