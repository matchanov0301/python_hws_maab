lst = [1, 2, 3, 4, 5, 6]
size = 2
nested_list = [lst[i:i+size] for i in range(0, len(lst), size)]
print(nested_list)