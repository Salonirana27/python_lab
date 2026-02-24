# Create student marks dictionary and find topper.

def find_topper(student_dict):
    topper = ""
    highest = -1
    for name in student_dict:
        if student_dict[name] > highest:
            highest = student_dict[name]
            topper = name
    return topper

# Taking input
n = int(input("Enter number of students: "))
students = {}

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))
    students[name] = marks

# Finding topper
topper = find_topper(students)

# Printing result
print("Topper is:", topper)

# output
# Enter number of students: 3
# Enter student name: A
# Enter marks: 85
# Enter student name: B
# Enter marks: 92
# Enter student name: C
# Enter marks: 78
# Topper is: B