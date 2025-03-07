lst = [1, 2, 3, 4, 5, 6]
sub = [3, 4]
exists = any(lst[i:i+len(sub)] == sub for i in range(len(lst) - len(sub) + 1))
print(exists)
