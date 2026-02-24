#check prime number using function
# Function to check prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Read input
num = int(input("enter number: "))

# Check and print result
if is_prime(num):
    print("Prime")
else:
    print("Not Prime")
    #output
    """enter number: 24
        Not Prime
        
        """