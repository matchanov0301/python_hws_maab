lst = [1, 2, 3, 2, 4, 2, 5]
element = 2
indices = [i for i in range(len(lst)) if lst[i] == element]
print(indices)