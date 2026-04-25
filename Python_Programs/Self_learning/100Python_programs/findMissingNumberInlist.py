# Program to find missing number from 1 to n

n = int(input("Enter value of n: "))
lst = list(map(int, input("Enter elements: ").split()))

expected_sum = n * (n + 1) // 2
actual_sum = sum(lst)

print("Missing Number:", expected_sum - actual_sum)

# Output:
# Enter value of n: 5
# Enter elements: 1 2 4 5
# Missing Number: 3