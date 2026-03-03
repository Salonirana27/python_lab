# Program to demonstrate simple class and object

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

# Taking input
name = input("Enter student name: ")
marks = int(input("Enter marks: "))

s1 = Student(name, marks)
s1.display()

#   Output:
# Enter student name: Saloni
# Enter marks: 85
# Name: Saloni
# Marks: 85