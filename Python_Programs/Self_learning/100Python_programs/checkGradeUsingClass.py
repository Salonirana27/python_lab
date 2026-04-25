# Program to calculate grade using class

class Grade:
    def __init__(self, marks):
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        else:
            return "Fail"

marks = int(input("Enter marks: "))
g = Grade(marks)

print("Grade:", g.calculate_grade())

# Output:
# Enter marks: 82
# Grade: B