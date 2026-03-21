def postorder_traversal(root):
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)            # Visit left
        dfs(node.right)           # Visit right
        result.append(node.val)   # Visit root
    dfs(root)
    return result

