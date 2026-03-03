# Program to check if substring exists

main_string = input("Enter main string: ")
sub_string = input("Enter substring: ")

if sub_string in main_string:
    print("Substring Found")
else:
    print("Substring Not Found")

# output:
# Enter main string: hello world
# Enter substring: world
# Substring Found