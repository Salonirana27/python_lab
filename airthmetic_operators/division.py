print("------ Division Program ------")

try:
    num1 = float(input("Enter first number (Dividend): "))
    num2 = float(input("Enter second number (Divisor): "))

    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print("Result =", result)

except ValueError:
    print("Invalid input! Please enter numeric values only.")
    
    
    #output
    """------ Division Program ------
Enter first number (Dividend): 34
Enter second number (Divisor): 2
Result = 17.0"""