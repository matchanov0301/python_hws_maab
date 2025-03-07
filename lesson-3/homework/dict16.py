my_dict = {"a": 1, "b": {"c": 2}}
has_nested = any(isinstance(v, dict) for v in my_dict.values())
print(has_nested)

