# Program to reverse file content

filename = input("Enter file name: ")

with open(filename, "r") as file:
    content = file.read()

reversed_content = content[::-1]

print("Reversed Content:")
print(reversed_content)

# Output:
# Enter file name: sample.txt
# Reversed Content:
# ACM emocleW
#avaJ olleH