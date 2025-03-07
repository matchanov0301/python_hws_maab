tpl = (3, 1, 4, 2, 5)
element = 2
if element in tpl:
    lst = list(tpl)
    lst.remove(element)
    tpl = tuple(lst)
print(tpl)
