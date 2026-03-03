# Program to sort list of dictionaries by 'age'

students = [
    {"name": "Aman", "age": 22},
    {"name": "Riya", "age": 20},
    {"name": "Karan", "age": 25}
]

sorted_students = sorted(students, key=lambda x: x["age"])

print("Sorted by Age:", sorted_students)

#  Output:
# Sorted by Age: [{'name': 'Riya', 'age': 20},
#                 {'name': 'Aman', 'age': 22},
#                 {'name': 'Karan', 'age': 25}]