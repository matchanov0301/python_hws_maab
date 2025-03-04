num = int(input("Enter a number: "))

positive = num > 0
even = num % 2 == 0

if positive and even:
    print("positive and even.")
else:
    print("not both positive and even.")
