# Program to count occurrences after sorting

lst = list(map(int, input("Enter elements: ").split()))

lst.sort()

count_dict = {}

for num in lst:
    count_dict[num] = count_dict.get(num, 0) + 1

print("Element Frequencies:", count_dict)

#  Output:
# Enter elements: 2 3 2 4 3 2
# Element Frequencies: {2:3, 3:2, 4:1}