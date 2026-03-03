# Program using namedtuple

from collections import namedtuple

Student = namedtuple("Student", ["name", "marks"])

name = input("Enter name: ")
marks = int(input("Enter marks: "))

s = Student(name, marks)

print("Name:", s.name)
print("Marks:", s.marks)

# Output:
# Enter name: Saloni
# Enter marks: 88
# Name: Saloni
# Marks: 88