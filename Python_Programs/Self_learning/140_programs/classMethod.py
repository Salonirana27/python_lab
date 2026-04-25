# Program demonstrating class method

class Student:
    school_name = "MIET"

    @classmethod
    def get_school(cls):
        return cls.school_name

print("School Name:", Student.get_school())

# Output:
# School Name: MIET