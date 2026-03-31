# Problem 21: Create a pie chart for percentage distribution

import matplotlib.pyplot as plt

# Taking input
categories = input("Enter categories: ").split()
values = list(map(int, input("Enter values: ").split()))

# Create pie chart
plt.pie(values, labels=categories, autopct='%1.1f%%')

# Title
plt.title("Pie Chart")

# Display chart
plt.show()

# Output:
# Enter categories: Food Travel Rent Shopping
# Enter values: 30 20 25 25
# A pie chart is displayed showing percentage distribution