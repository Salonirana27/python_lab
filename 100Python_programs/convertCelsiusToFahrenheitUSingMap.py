# Program to convert list of Celsius values to Fahrenheit using map

n = int(input("Enter number of temperature values: "))
temps = []

for i in range(n):
    temps.append(float(input("Enter temperature in Celsius: ")))

fahrenheit = list(map(lambda c: (c * 9/5) + 32, temps))

print("Temperatures in Fahrenheit:", fahrenheit)

# Output:
# Enter number of temperature values: 2
# 0
# 100
# Temperatures in Fahrenheit: [32.0, 212.0]