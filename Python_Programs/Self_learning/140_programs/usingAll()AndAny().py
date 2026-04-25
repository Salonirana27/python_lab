# Program demonstrating all() and any()

numbers = list(map(int, input("Enter numbers: ").split()))

print("All numbers are positive:", all(n > 0 for n in numbers))
print("Any number is negative:", any(n < 0 for n in numbers))

# Output:
# Enter numbers: 1 2 3 -1
# All numbers are positive: False
# Any number is negative: True