tpl = (1, 2, 3, 2, 4, 2, 5)
element = 2
indices = [i for i in range(len(tpl)) if tpl[i] == element]
print(indices)
