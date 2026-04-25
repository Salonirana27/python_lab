# Salary Processing System

salaries = list(map(float, input("Enter salaries separated by space: ").split()))
minimum_wage = float(input("Enter minimum wage: "))

# Remove salaries below minimum wage
valid_salaries = [s for s in salaries if s >= minimum_wage]

# Add 5% bonus
for i in range(len(valid_salaries)):
    if valid_salaries[i] > 50000:
        valid_salaries[i] *= 1.05

# Sort descending
valid_salaries.sort(reverse=True)

print("Processed Salaries:", valid_salaries)
print("Top 3 Highest Salaries:", valid_salaries[:3])

#output
"""Enter salaries separated by space: 30000 55000 70000 20000 80000
Enter minimum wage: 25000
Processed Salaries: [84000.0, 73500.0, 57750.0, 30000.0]
Top 3 Highest Salaries: [84000.0, 73500.0, 57750.0]"""