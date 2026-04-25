# Program demonstrating generator function

def generate_numbers(n):
    for i in range(1, n + 1):
        yield i

num = int(input("Enter limit: "))

for value in generate_numbers(num):
    print(value)

# Output:
# Enter limit: 3
# 1
# 2
# 3