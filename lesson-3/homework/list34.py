lst = [1, 2, 3, 4, 5]
steps = 2
rotated = lst[-steps:] + lst[:-steps]
print(rotated)
