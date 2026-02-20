import threedfigures

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

print("Curved Surface Area =", threedfigures.cylinder_csa(r, h))
print("Total Surface Area =", threedfigures.cylinder_tsa(r, h))
print("Volume =", threedfigures.cylinder_volume(r, h))