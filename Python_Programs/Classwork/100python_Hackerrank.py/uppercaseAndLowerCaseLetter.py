# Program to count uppercase and lowercase letters

text = input("Enter a string: ")

upper = 0
lower = 0

for ch in text:
    if ch.isupper():
        upper = upper + 1
    elif ch.islower():
        lower = lower + 1

print("Uppercase letters =", upper)
print("Lowercase letters =", lower)

#Output
#Enter a string: HelloWorld
#Uppercase letters = 2
#Lowercase letters = 8