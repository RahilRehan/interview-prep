def inorder_traversal(node: BinaryTreeNode) -> List[int]:
    stack, result = [], []

    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.data)
            node = node.right

    return result