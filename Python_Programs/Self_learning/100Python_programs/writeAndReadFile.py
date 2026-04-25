# Program to write and then read file

text = input("Enter text: ")

with open("data.txt", "w") as file:
    file.write(text)

with open("data.txt", "r") as file:
    content = file.read()

print("File Content:", content)

# Output:
# Enter text: Hello MCA
# File Content: Hello MCA