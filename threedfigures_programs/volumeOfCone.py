import threedfigures

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

print("Curved Surface Area =", threedfigures.cone_csa(r, h))
print("Total Surface Area =", threedfigures.cone_tsa(r, h))
print("Volume =", threedfigures.cone_volume(r, h))