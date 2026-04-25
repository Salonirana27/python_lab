# Problem 24: Create scatter plot and highlight maximum point

import matplotlib.pyplot as plt

# Taking input
x = list(map(int, input("Enter x values: ").split()))
y = list(map(int, input("Enter y values: ").split()))

# Create scatter plot
plt.scatter(x, y)

# Find maximum y value and its index
max_y = max(y)
max_index = y.index(max_y)

# Highlight maximum point
plt.scatter(x[max_index], y[max_index], marker='o')

# Labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot")

# Display graph
plt.show()

# Output:
# Enter x values: 1 2 3 4 5
# Enter y values: 10 25 15 30 20
# A scatter plot is displayed and the highest point is highlighted