import threedfigures

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

print("Curved Surface Area =", threedfigures.cylinder_csa(r, h))
print("Total Surface Area =", threedfigures.cylinder_tsa(r, h))
print("Volume =", threedfigures.cylinder_volume(r, h))

#output
"""Enter radius: 8
Enter height: 4
Curved Surface Area = 201.06192982974676
Total Surface Area = 603.1857894892403
Volume = 804.247719318987"""