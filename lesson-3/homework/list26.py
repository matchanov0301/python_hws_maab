lst = [1, 2, 3, 4, 5, 6]
mid = len(lst) // 2
if len(lst) % 2 == 0:
    print(lst[mid-1:mid+1])
else:
    print(lst[mid])