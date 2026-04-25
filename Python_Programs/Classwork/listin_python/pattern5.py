n = int(input("enter number of rows: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
    
    #output
    """enter number of rows: 5
1
12
123
1234
12345 """