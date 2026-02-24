#check number is armstrong or not
num = int(input("enter number: "))

temp = abs(num)
digits = len(str(temp))
total = 0
original = temp

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == original:
    print("Armstrong")
else:
    print("Not Armstrong")
    
    #output
    """enter number: 23
Not Armstrong 
enter number: 153 
Armstrong
"""