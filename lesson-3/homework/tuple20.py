tpl = (1, 2, 3, 4, 5, 6)
size = 2
nested_tpl = tuple(tpl[i:i+size] for i in range(0, len(tpl), size))
print(nested_tpl)
