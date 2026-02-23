# E-Commerce Cart System

prices = list(map(float, input("Enter product prices separated by space: ").split()))

# Remove duplicate items
unique_prices = list(set(prices))

total = sum(unique_prices)

# Apply discount
if total > 5000:
    total *= 0.90

# Add GST 18%
total *= 1.18

print("Unique Prices:", unique_prices)
print("Final Payable Amount: ₹", round(total, 2))

#output
"""Enter product prices separated by space:
2000 1500 2000 1800
Unique Prices: [2000.0, 1500.0, 1800.0]
Final Payable Amount: ₹ 7434.0"""