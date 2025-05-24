def deepest_nesting(lst):
    current_level = [lst]
    depth = 0

    while current_level:
        next_level = []
        for item in current_level:
            if isinstance(item, list):
                next_level.extend(item)
        if next_level:
            depth += 1
        current_level = next_level

    return depth
lst = [1, [2, [3, [4, []]], 5]]
print(deepest_nesting(lst))