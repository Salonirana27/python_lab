# Student Marks Analyzer

marks = list(map(int, input("Enter student marks separated by space: ").split()))

# Remove invalid marks
valid_marks = [m for m in marks if 0 <= m <= 100]

if not valid_marks:
    print("No valid marks available.")
else:
    average = sum(valid_marks) / len(valid_marks)

    topper = max(valid_marks)
    toppers = [m for m in valid_marks if m == topper]

    # Grade based on average
    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 50:
        grade = "C"
    else:
        grade = "D"

    print("Valid Marks:", valid_marks)
    print("Average:", round(average, 2))
    print("Topper Marks:", toppers)
    print("Overall Grade:", grade)
    
    #output
    """Enter student marks separated by space:
95 88 76 102 -5 89 95
Valid Marks: [95, 88, 76, 89, 95]
Average: 88.6
Topper Marks: [95, 95]
Overall Grade: B"""