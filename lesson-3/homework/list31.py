lst = [1, 2, 3]
n = 3
repeated = [x for x in lst for _ in range(n)]
print(repeated)