# Program to generate random number

import random

start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

number = random.randint(start, end)

print("Random Number:", number)

# Output:
# Enter start range: 1
# Enter end range: 10
# Random Number: 7