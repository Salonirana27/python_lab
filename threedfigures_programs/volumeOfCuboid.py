import threedfigures

l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))

print("Curved Surface Area =", threedfigures.cuboid_csa(l, b, h))
print("Total Surface Area =", threedfigures.cuboid_tsa(l, b, h))
print("Volume =", threedfigures.cuboid_volume(l, b, h))

#output
"""Enter length: 23
Enter breadth: 24
Enter height: 34
Curved Surface Area = 3196.0
Total Surface Area = 4300.0
Volume = 18768.0"""