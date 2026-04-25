# Program to check whether string is palindrome

text = input("Enter a string: ")
rev = ""

for ch in text:
    rev = ch + rev

if text == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
#Output


#Enter a string: madam
#Palindrome