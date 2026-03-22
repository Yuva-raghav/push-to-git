def min_depth(root):
    if root is None:
        return 0

    left = min_depth(root.get("left"))
    right = min_depth(root.get("right"))

    if not root.get("left"):
        return 1 + right
    if not root.get("right"):
        return 1 + left

    return 1 + min(left, right)

tree = {
    "val": 1,
    "left": {"val": 2, "left": None, "right": None},
    "right": {"val": 3, "left": None, "right": None}
}

print(min_depth(tree))  # Output: 2
