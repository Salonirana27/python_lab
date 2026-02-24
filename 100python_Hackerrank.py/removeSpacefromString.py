# Program to remove spaces from string

text = input("Enter a string: ")
new_text = ""

for ch in text:
    if ch != " ":
        new_text = new_text + ch

print("String without spaces:", new_text)
#Output
#Enter a string: hello world
#String without spaces: helloworld