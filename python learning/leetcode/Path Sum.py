def has_path_sum(root, targetSum):
    if root is None:
        return False

    if root.get("left") is None and root.get("right") is None:
        return targetSum == root["val"]

    return (has_path_sum(root.get("left"), targetSum - root["val"]) or
            has_path_sum(root.get("right"), targetSum - root["val"]))

tree = {
    "val": 5,
    "left": {
        "val": 4,
        "left": {"val": 11, "left": {"val": 7}, "right": {"val": 2}}
    },
    "right": {
        "val": 8,
        "left": {"val": 13},
        "right": {"val": 4, "right": {"val": 1}}
    }
}

print(has_path_sum(tree, 22))  # Output: True
