#reverse a string using for loop

text = input("enter string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

print("the reverse string is:",reverse)

#output
"""enter string: saloni
the reverse string is: inolas"""