# Program to calculate total, average and grade

name = input("Enter student name: ")
marks = []

for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

total = sum(marks)
average = total / 5

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "D"

print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)

# Output:
# Enter student name: Saloni
# Enter marks: 80 85 90 75 70
# Total Marks: 400
# Average: 80
# Grade: B