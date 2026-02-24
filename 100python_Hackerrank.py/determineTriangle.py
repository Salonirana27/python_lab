#determine the type of triangle
a = float(input("enter value: "))
b = float(input("enter value: "))
c = float(input("enter value: "))

# Check triangle validity
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Invalid Triangle")
    
    #output
    """enter value: 3
enter value: 3
enter value: 3
Equilateral Triangle

enter value: 3
enter value: 4
enter value: 5
Scalene Triangle

nter value: 5
enter value: 5
enter value: 3
Isosceles Triangle


"""