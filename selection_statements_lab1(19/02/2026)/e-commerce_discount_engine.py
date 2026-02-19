cart_value = float(input("Enter cart value: "))
membership = input("Enter membership (Silver/Gold/Platinum): ")
festival = input("Is it festival season? (yes/no): ")

discounts = []

# Cart value discount
if cart_value > 50000:
    discounts.append(20)
elif cart_value > 20000:
    discounts.append(10)
else:
    discounts.append(5)

# Membership discount
if membership.lower() == "silver":
    discounts.append(5)
elif membership.lower() == "gold":
    discounts.append(10)
elif membership.lower() == "platinum":
    discounts.append(15)

# Festival discount
if festival.lower() == "yes":
    discounts.append(10)

max_discount = max(discounts)

final_amount = cart_value - (cart_value * max_discount / 100)

print("Highest Discount Applied:", max_discount, "%")
print("Final Payable Amount:", final_amount)