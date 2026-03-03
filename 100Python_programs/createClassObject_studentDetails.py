# Program to create a class and object for student details

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Student Marks:", self.marks)

# Taking input
name = input("Enter student name: ")
marks = int(input("Enter student marks: "))

# Creating object
s1 = Student(name, marks)

# Calling method
s1.display()

# Output:
# Enter student name: Saloni
# Enter student marks: 85
# Student Name: Saloni
# Student Marks: 85