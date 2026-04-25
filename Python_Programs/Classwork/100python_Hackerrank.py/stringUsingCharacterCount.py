# Program to compress string using character counts

text = input("Enter a string: ")
result = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count = count + 1
    else:
        result = result + text[i - 1] + str(count)
        count = 1

result = result + text[-1] + str(count)

print("Compressed string:", result)

#Output
#Enter a string: aaabbc
#Compressed string: a3b2c1