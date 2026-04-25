# Program to find average of list elements

lst = list(map(int, input("Enter elements: ").split()))

total = 0
count = 0

for num in lst:
    total += num
    count += 1

average = total / count

print("Average:", average)

#Output:
# Enter elements: 10 20 30
# Average: 20.0