# Program to find sum of prime numbers up to N

n = int(input("Enter a number: "))
sum_prime = 0

for num in range(2, n + 1):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        sum_prime += num

print("Sum of prime numbers:", sum_prime)

# Output:
# Enter a number: 10
# Sum of prime numbers: 17