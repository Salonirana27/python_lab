# Program to count frequency manually

n = int(input("Enter number of elements: "))
lst = list(map(int, input("Enter elements: ").split()))

frequency = {}

for item in lst:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("Frequency Dictionary:", frequency)

#Output:
# Enter number of elements: 5
# Enter elements: 1 2 2 3 1
# Frequency Dictionary: {1:2, 2:2, 3:1}