a = input("Enter a word to check palindrome: ")
if a.lower() == a[::-1].lower():
    print("Palindrome")
else:
    print("Not a palindrome")