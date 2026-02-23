# Online Exam Result Processor

scores = list(map(int, input("Enter student scores separated by space: ").split()))

# Remove lowest 2 scores
scores.sort()
scores = scores[2:] if len(scores) > 2 else []

# Add grace marks
for i in range(len(scores)):
    if 30 <= scores[i] <= 35:
        scores[i] += 5

passed = len([s for s in scores if s >= 40])

print("Updated Scores:", scores)
print("Number of Students Passed:", passed)

#output
""" Enter student scores separated by space: 25 32 34 45 50 60
Updated Scores: [39, 45, 50, 60]
Number of Students Passed: 3"""