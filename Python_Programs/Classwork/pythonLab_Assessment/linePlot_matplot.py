# Problem 19: Create a line plot using given x and y values

import matplotlib.pyplot as plt

# Taking input from user
x = list(map(int, input("Enter x values: ").split()))
y = list(map(int, input("Enter y values: ").split()))

# Create line plot
plt.plot(x, y)

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot")

# Display graph
plt.show()

# Output:
# Enter x values: 1 2 3 4 5
# Enter y values: 2 4 6 8 10
# A line graph is displayed connecting the given points