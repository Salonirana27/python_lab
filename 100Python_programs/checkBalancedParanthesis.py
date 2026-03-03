# Program to check balanced parentheses

expression = input("Enter expression: ")

stack = []
balanced = True

for ch in expression:
    if ch == "(":
        stack.append(ch)
    elif ch == ")":
        if stack:
            stack.pop()
        else:
            balanced = False
            break

if balanced and not stack:
    print("Balanced")
else:
    print("Not Balanced")

# Output:
# Enter expression: (())
# Balanced