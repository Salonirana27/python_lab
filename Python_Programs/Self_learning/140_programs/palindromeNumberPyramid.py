# Program to print palindrome number pyramid

n = int(input("Enter number of rows: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    
    for j in range(1, i + 1):
        print(j, end="")
    
    for j in range(i - 1, 0, -1):
        print(j, end="")
    
    print()

#  Output:
# Enter number of rows: 4
#    1
#   121
#  12321
# 1234321