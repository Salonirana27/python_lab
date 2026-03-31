# Problem 20: Create a bar chart for product sales

import matplotlib.pyplot as plt

# Taking input
products = input("Enter product names: ").split()
sales = list(map(int, input("Enter sales values: ").split()))

# Create bar chart
plt.bar(products, sales)

# Labels and title
plt.xlabel("Products")
plt.ylabel("Sales")
plt.title("Product Sales")

# Show chart
plt.show()

# Output:
# Enter product names: A B C D E
# Enter sales values: 10 20 15 25 30
# A bar chart is displayed showing sales of each product