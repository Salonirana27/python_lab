#swapping of two numbers without using  third variable
a = int(input("Enter the value of a:"))
b = int (input("Enter the value of b:"))

a = a+b
b = a-b
a = a-b 
print("after swapping---------------")
print("a=",a)
print("b=",b)

#output
"""Enter the value of a:5
Enter the value of b:6
after swapping---------------
a= 6
b= 5 """