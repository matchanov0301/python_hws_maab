tpl = (1, 2, 3)
n = 3
repeated = tuple(x for x in tpl for _ in range(n))
print(repeated)
