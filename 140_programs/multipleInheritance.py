# Program demonstrating multiple inheritance

class Father:
    def skills1(self):
        print("Gardening")

class Mother:
    def skills2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skills1()
c.skills2()

#  Output:
# Gardening
# Cooking