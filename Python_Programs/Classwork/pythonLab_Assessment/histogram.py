# Problem 22: Plot a histogram for a dataset

import matplotlib.pyplot as plt

# Taking input from user
data = list(map(int, input("Enter dataset: ").split()))

# Create histogram
plt.hist(data, bins=5)

# Labels and title
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram")

# Display graph
plt.show()

# Output:
# Enter dataset: 1 2 2 3 3 3 4 4 5 5 5 5
# A histogram is displayed showing frequency distribution of the data