# Program demonstrating single inheritance

class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Subject:", self.subject)

name = input("Enter teacher name: ")
subject = input("Enter subject: ")

t1 = Teacher(name, subject)
t1.display()

# Output:
# Enter teacher name: Saloni
# Enter subject: Python
# Name: Saloni
# Subject: Python