# -----------------------------------------------------------
# Problem 5: Sort list of tuples based on marks
# -----------------------------------------------------------

def sort_by_marks(data):
    # Sort using lambda (based on second value = marks)
    return sorted(data, key=lambda x: x[1])


# Input
n = int(input("Enter number of students: "))
data = []

# Taking name and marks
for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    data.append((name, marks))

# display  Output
print("Sorted List:", sort_by_marks(data))

# Output:
#Enter number of students: 3
#Enter name: saloni
#Enter marks: 99
#Enter name: anshika
#Enter marks: 90
#Enter name: sneha
#Enter marks: 89
#Sorted List: [('sneha', 89), ('anshika', 90), ('saloni', 99)]
