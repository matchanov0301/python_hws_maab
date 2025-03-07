from collections import defaultdict
default_dict = defaultdict(lambda: "Not Found")
default_dict["a"] = 10
print(default_dict["b"])
