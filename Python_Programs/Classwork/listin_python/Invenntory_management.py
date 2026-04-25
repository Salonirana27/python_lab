# Inventory Management

stocks = list(map(int, input("Enter stock quantities separated by space: ").split()))

# Remove zero stock
stocks = [s for s in stocks if s > 0]

# Restock items below 10
for i in range(len(stocks)):
    if stocks[i] < 10:
        stocks[i] += 50

total_inventory = sum(stocks)

print("Updated Stock:", stocks)
print("Total Inventory Count:", total_inventory)

#output
""" nter stock quantities separated by space: 0 5 8 20 0 3
Updated Stock: [55, 58, 20, 53]
Total Inventory Count: 186"""