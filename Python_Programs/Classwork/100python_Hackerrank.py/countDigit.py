#count digit from a number
num = int(input("enter the number: "))

num = abs(num)

if num == 0:
    print(1)
else:
    count = 0
    while num > 0:
        num //= 10
        count += 1
    print("the count is: ", count)
    
    #output
    """enter the number: 123456
the count is:  6 """