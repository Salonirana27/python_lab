# Program to count number of objects created

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

# Creating objects
n = int(input("Enter number of objects to create: "))

for i in range(n):
    obj = Counter()

print("Total Objects Created:", Counter.count)

# Output:
# Enter number of objects to create: 3
# Total Objects Created: 3