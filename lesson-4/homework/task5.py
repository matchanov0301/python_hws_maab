while True:
    password = input("Enter a password: ")

    if len(password) < 8:
        print("Password is too short.")
    elif not any(char.isupper() for char in password):
        print("Password must contain an uppercase letter.")
    else:
        print("Password is strong.")
        break  # Exit loop when password is strong
