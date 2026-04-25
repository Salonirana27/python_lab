# Program demonstrating basic decorator

def decorator_function(func):
    def wrapper():
        print("Before Function Execution")
        func()
        print("After Function Execution")
    return wrapper

@decorator_function
def say_hello():
    print("Hello!")

say_hello()

# Output:
# Before Function Execution
# Hello!
# After Function Execution
