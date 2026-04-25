#check the number lies in given range 
num = float(input("Enter Number: "))
lower = float(input("Enter lower : "))
upper = float(input("Enter Upper: "))

if lower <= num <= upper:
    print("Within Range")
else:
    print("Out of Range")
    
    #output
    """Enter Number: 5
Enter lower : 1
Enter Upper: 10
Within Range

Enter Number: 20
Enter lower : 30
Enter Upper: 10
Out of Range

"""