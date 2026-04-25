# Program to count prime numbers in list

lst = list(map(int, input("Enter elements: ").split()))

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

count = 0

for num in lst:
    if is_prime(num):
        count += 1

print("Number of prime elements:", count)

# Output:
# Enter elements: 2 3 4 5 6
# Number of prime elements: 3