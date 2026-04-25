# Program to write list elements into file

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(input("Enter element: "))

file = open("listdata.txt", "w")

for item in lst:
    file.write(item + "\n")

file.close()

print("List data written successfully")

# Output:
# Enter number of elements: 2
# Apple
# Mango
# List data written successfully