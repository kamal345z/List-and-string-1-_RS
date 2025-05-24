lst = ["abc", "def", ["ghi", "jkl"]]
r = []
for item in lst:
    if type(item) == list:
        for subitem in item:
            for char in subitem:
                r.append(char)
    else:
        for char in item:
            r.append(char)
print("Flattened list is :", r)