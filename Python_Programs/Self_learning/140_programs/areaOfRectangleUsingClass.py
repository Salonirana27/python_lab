# Program using class to calculate area of rectangle

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

l = float(input("Enter length: "))
w = float(input("Enter width: "))

r = Rectangle(l, w)
print("Area:", r.area())

#  Output:
# Enter length: 5
# Enter width: 3
# Area: 15.0