# Check whether a given year is a leap year
year = int(input("enter year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(" This is Leap Year",year)
else:
    print("This is Not a Leap Year",year)
    
    #output
    """enter year: 2026
       This is Not a Leap Year 2026"""