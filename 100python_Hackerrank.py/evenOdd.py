#Check whether a number is even or odd without modulus operator

num = int(input("Enter an integer: "))

# Check whether the number is even or odd without using modulus
if (num // 2) * 2 == num:
    print("The given number is Even " )
else:
    print("The given number is Odd " )
    
    #output
    """Enter an integer: 28
The given number is Even """