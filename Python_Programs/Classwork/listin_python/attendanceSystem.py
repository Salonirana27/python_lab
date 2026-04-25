# Attendance Tracker

attendance = list(map(int, input("Enter attendance (1 for present, 0 for absent): ").split()))

total_days = len(attendance)
present_days = attendance.count(1)

percentage = (present_days / total_days) * 100 if total_days > 0 else 0

print("Attendance Percentage:", round(percentage, 2), "%")

if percentage < 75:
    print("Warning: Attendance below 75%")

# Replace consecutive absences with "Warning"
for i in range(1, len(attendance)):
    if attendance[i] == 0 and attendance[i-1] == 0:
        attendance[i] = "Warning"

print("Updated Attendance Record:", attendance)

#output
"""Enter attendance (1 for present, 0 for absent): 1 1 1 1 1 0 0 0
Attendance Percentage: 62.5 %
Warning: Attendance below 75%
Updated Attendance Record: [1, 1, 1, 1, 1, 0, 'Warning', 0]"""