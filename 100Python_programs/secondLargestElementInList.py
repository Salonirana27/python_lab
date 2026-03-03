# Program to find second largest element without using sort()

n = int(input("Enter number of elements: "))
lst = list(map(int, input("Enter elements: ").split()))

largest = second = float('-inf')

for num in lst:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second Largest Element:", second)

#Output:
# Enter number of elements: 5
# Enter elements: 10 20 5 8 15
# Second Largest Element: 15