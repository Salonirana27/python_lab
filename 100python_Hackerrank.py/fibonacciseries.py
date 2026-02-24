#generate fibonacci series using while loop
n = int(input("enter the number: "))

a = 0
b = 1
count = 0

while count < n:
    print(a)
    c = a + b
    a = b
    b = c
    count += 1
    
    #output
    """enter the number: 10
0
1
1
2
3
5
8
13
21
34"""
