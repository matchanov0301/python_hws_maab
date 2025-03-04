txt = input("enter a word: ")
ch = input("enter a character to remove: ")
if ch in txt:
    print(txt.replace(ch, ""))
else:
    print("character is not in here")