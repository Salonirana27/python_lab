# find profit and loss 
cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

if selling_price > cost_price:
    print("Profit =", selling_price - cost_price)
elif selling_price < cost_price:
    print("Loss =", cost_price - selling_price)
else:
    print("No Profit, No Loss")
    
    #output
    """Enter Cost Price: 56
Enter Selling Price: 76
Profit = 20.0"""