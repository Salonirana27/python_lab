print("------ Floor Division Program ------")

try:
    num1 = float(input("Enter first number (Dividend): "))
    num2 = float(input("Enter second number (Divisor): "))

    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 // num2
        print("Floor Division Result =", result)

except ValueError:
    print("Invalid input! Please enter numeric values only.")
    
    #output
    """------ Floor Division Program ------
Enter first number (Dividend): 26
Enter second number (Divisor): 0
Error: Division by zero is not allowed."""