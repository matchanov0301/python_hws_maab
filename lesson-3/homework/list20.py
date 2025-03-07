lst = [3, 1, 4, 2, 5, 5]
unique = sorted(set(lst), reverse=True)
if len(unique) > 1:
    print(unique[1])
