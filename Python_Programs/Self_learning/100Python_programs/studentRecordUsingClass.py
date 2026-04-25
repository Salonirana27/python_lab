# Program to store student records using class

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

n = int(input("Enter number of students: "))

students = []

for i in range(n):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    students.append(Student(name, marks))

print("\nStudent Records:")
for s in students:
    s.display()
    print()

# Output:
# Enter number of students: 1
# Enter name: Saloni
# Enter marks: 88
# Student Records:
# Name: Saloni
# Marks: 88