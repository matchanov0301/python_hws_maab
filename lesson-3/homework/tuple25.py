tpl = (1, 2, 2, 3, 4, 3, 5, 1)
unique_ordered = []
for x in tpl:
    if x not in unique_ordered:
        unique_ordered.append(x)
unique_tpl = tuple(unique_ordered)
print(unique_tpl)