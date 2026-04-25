# using append and extend in this
# list of 5 numbers
numbers = [76, 34, 36, 56, 59]

# APPEND METHOD
print("----- APPEND METHOD -----")
numbers.append(150)
print("after inserting the list is:", numbers)

print("-------------")

# creating a list of five numbers again
list2 = [23, 45, 32, 22, 57]
numbers.append(list2)
print("after inserting list2:\n", numbers)

# EXTEND METHOD
print("----- USING EXTEND METHOD -----")
list3 = [7, 34, 54, 21, 12]
numbers.extend(list3)
print("after extending list3:\n", numbers)

# INSERT METHOD
print("----- USING INSERT METHOD -----")
numbers.insert(3, 670)
print("after inserting an element:", numbers)

#output
"""----- APPEND METHOD -----
after inserting the list is: [76, 34, 36, 56, 59, 150]
-------------
after inserting list2:
 [76, 34, 36, 56, 59, 150, [23, 45, 32, 22, 57]]
----- USING EXTEND METHOD -----
after extending list3:
 [76, 34, 36, 56, 59, 150, [23, 45, 32, 22, 57], 7, 34, 54, 21, 12]
----- USING INSERT METHOD -----
after inserting an element: [76, 34, 36, 670, 56, 59, 150, [23, 45, 32, 22, 57], 7, 34, 54, 21, 12]"""