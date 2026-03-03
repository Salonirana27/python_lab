# Program to calculate electricity bill using nested if

units = int(input("Enter electricity units: "))

if units <= 100:
    bill = units * 2
else:
    if units <= 300:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 200 * 3 + (units - 300) * 5

print("Total Bill:", bill)

# Output:
# Enter electricity units: 250
# Total Bill: 650