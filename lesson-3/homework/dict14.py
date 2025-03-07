my_dict = {"a": 1, "b": 2, "c": 1}
value_to_find = 1
keys = [k for k, v in my_dict.items() if v == value_to_find]
print(keys)

