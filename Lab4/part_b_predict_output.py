"""Part B - Predict the output before running each snippet."""

# 1
d = {"a": 1, "b": 2}
d2 = d
d2["c"] = 3
print(len(d))  # 3

# 2
d = {"x": [1]}
e = d.copy()
e["x"].append(2)
print(d)  # {'x': [1, 2]}

# 3
print({k: v for k, v in zip("abc", range(3)) if v})  # {'b': 1, 'c': 2}

# 4
d = {"a": 1}
print(d.setdefault("a", 9), d.setdefault("b", 5), d)
# 1 5 {'a': 1, 'b': 5}

# 5
d = {1: "a", 1.0: "b", True: "c"}
print(d, len(d))  # {1: 'c'} 1

# 6
d = {"a": 1, "b": 2, "c": 3}
try:
    for k in d:
        if d[k] == 2:
            del d[k]
except RuntimeError as error:
    print(type(error).__name__ + ":", error)
# The exception is caught here so questions 7 and 8 can also run.

# 7
d = {"a": 1, "b": 2}
print(d.pop("z", None), d.popitem())  # None ('b', 2)

# 8
print({v: k for k, v in {"a": 1, "b": 1}.items()})  # {1: 'b'}
