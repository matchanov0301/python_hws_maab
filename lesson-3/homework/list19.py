lst = [1, 2, 3, 4, 2, 5]
old = 2
new = 9
if old in lst:
    lst[lst.index(old)] = new
print(lst)