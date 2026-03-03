# Program using itertools.count()

import itertools

start = int(input("Enter starting number: "))
step = int(input("Enter step value: "))

counter = itertools.count(start, step)

for i in range(5):
    print(next(counter))

# Output:
# Enter starting number: 10
# Enter step value: 2
# 10
# 12
# 14
# 16
# 18