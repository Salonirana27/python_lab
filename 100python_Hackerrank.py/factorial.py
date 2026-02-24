#find factorial using while loop 
n = int(input("enter the value: "))

if n < 0:
    print("Invalid Input")
else:
    fact = 1
    i = 1
    while i <= n:
        fact *= i
        i += 1
    print(fact)
    
    #output
    """enter the value: 1
1

enter the value: 4
24 
"""
