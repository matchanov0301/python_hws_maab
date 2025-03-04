username = input("Enter username: ")
password = input("Enter password: ")

valid = bool(username) and bool(password)

if valid:
    print("Login successful")
else:
    print("Username and password cannot be empty")
