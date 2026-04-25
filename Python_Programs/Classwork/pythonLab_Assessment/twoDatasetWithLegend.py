# Problem 23: Plot two datasets on the same graph with legend

import matplotlib.pyplot as plt

# Taking input
x = list(map(int, input("Enter x values: ").split()))
y1 = list(map(int, input("Enter first dataset: ").split()))
y2 = list(map(int, input("Enter second dataset: ").split()))

# Plot both datasets
plt.plot(x, y1, label="Dataset 1")
plt.plot(x, y2, label="Dataset 2")

# Labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Two Dataset Plot")

# Show legend
plt.legend()

# Display graph
plt.show()

# Output:
# Enter x values: 1 2 3 4
# Enter first dataset: 2 4 6 8
# Enter second dataset: 1 3 5 7
# A graph is displayed with two lines and a legend