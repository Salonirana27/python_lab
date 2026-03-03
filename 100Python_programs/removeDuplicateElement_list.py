# Program to remove duplicates manually

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    element = int(input("Enter element: "))
    lst.append(element)

unique = []

for item in lst:
    if item not in unique:
        unique.append(item)

print("List after removing duplicates:", unique)

#Output:
# Enter number of elements: 5
# 1 2 2 3 4
# List after removing duplicates: [1, 2, 3, 4]