# Program to convert string to title case manually

sentence = input("Enter a sentence: ")
result = ""
new_word = True

for ch in sentence:
    if ch == " ":
        result = result + ch
        new_word = True
    else:
        if new_word:
            result = result + ch.upper()
            new_word = False
        else:
            result = result + ch.lower()

print("Title case:", result)

#Output
#Enter a sentence: hello world
#Title case: Hello World