# Program to find first non-repeating character

text = input("Enter a string: ")

for ch in text:
    if text.count(ch) == 1:
        print("First non-repeating character:", ch)
        break
    
#Output
#Enter a string: swiss
#First non-repeating character: w