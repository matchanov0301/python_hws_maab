lst = [1, 2, 2, 3, 4, 3, 5, 1]
unique_ordered = []
for x in lst:
    if x not in unique_ordered:
        unique_ordered.append(x)
print(unique_ordered)