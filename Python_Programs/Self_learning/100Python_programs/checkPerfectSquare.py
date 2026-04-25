# Program to check if a number is perfect square

num = int(input("Enter a number: "))

if int(num ** 0.5) ** 2 == num:
    print("Perfect Square")
else:
    print("Not a Perfect Square")

# Output:
# Enter a number: 25
# Perfect Square