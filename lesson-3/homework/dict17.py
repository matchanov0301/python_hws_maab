nested_dict = {"a": {"b": {"c": 5}}}
value = nested_dict.get("a", {}).get("b", {}).get("c", "Not Found")
print(value)

