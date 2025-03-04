txt = input("Enter a string: ")

if any(char.isdigit() for char in txt):
    print("The string contains digits.")
else:
    print("No digits.")