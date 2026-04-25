# Program demonstrating constructor and destructor

class Demo:
    def __init__(self):
        print("Constructor called")

    def __del__(self):
        print("Destructor called")

# Creating object
obj = Demo()

# Deleting object
del obj

# Output:
# Constructor called
# Destructor called