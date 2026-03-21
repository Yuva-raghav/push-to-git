def preorder_traversal(root):
    result = []
    def dfs(node):
        if not node:
            return
        result.append(node.val)   # Visit root
        dfs(node.left)            # Visit left
        dfs(node.right)           # Visit right
    dfs(root)
    return result

