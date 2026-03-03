# Program to print reverse pyramid

n = int(input("Enter number of rows: "))

for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)

# Output:
# Enter number of rows: 4
# * * * *
#  * * *
#   * *
#    *