import threedfigures

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

print("Curved Surface Area =", threedfigures.cone_csa(r, h))
print("Total Surface Area =", threedfigures.cone_tsa(r, h))
print("Volume =", threedfigures.cone_volume(r, h))

#output
"""Enter radius: 7
Enter height: 4
Curved Surface Area = 177.29830799381477
Total Surface Area = 331.2363480197146
Volume = 205.25072003453315"""