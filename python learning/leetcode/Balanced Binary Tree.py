def is_balanced(root):
    def height(node):
        if node is None:
            return 0
        left = height(node.get("left"))
        right = height(node.get("right"))

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    return height(root) != -1

tree = {
    "val": 1,
    "left": {"val": 2, "left": {"val": 3}, "right": {"val": 4}},
    "right": {"val": 5}
}

print(is_balanced(tree))  # Output: True
