# Problem 25: Customize plot with title, labels, and grid

import matplotlib.pyplot as plt

# Taking input
months = input("Enter months: ").split()
revenue = list(map(int, input("Enter revenue: ").split()))

# Create line plot
plt.plot(months, revenue)

# Customize graph
plt.title("Monthly Revenue")
plt.xlabel("Months")
plt.ylabel("Revenue")
plt.grid()

# Display graph
plt.show()

# Output:
# Enter months: Jan Feb Mar Apr May
# Enter revenue: 100 150 200 180 220
# A styled line graph is displayed with title, labels, and grid