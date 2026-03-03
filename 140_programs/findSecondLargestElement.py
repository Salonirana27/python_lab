# Program to find second largest element

lst = list(map(int, input("Enter elements: ").split()))

unique_lst = list(set(lst))
unique_lst.sort()

print("Second Largest Element:", unique_lst[-2])

#  Output:
# Enter elements: 10 20 30 40
# Second Largest Element: 30