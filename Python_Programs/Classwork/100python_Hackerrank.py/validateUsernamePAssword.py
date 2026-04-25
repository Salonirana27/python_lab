#validate username and password
username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Username or Password")
    
    #output
    """Enter username: amin    
Enter password: 1234
Invalid Username or Password 

Enter username: admin
Enter password: 1234
Login Successful

"""
