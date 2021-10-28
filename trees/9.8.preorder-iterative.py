def preorder_traversal(node: BinaryTreeNode) -> List[int]:
    stack, result = [], []
    while stack or node:
        if node:
            stack.append(node)
            result.append(node.data)
            node = node.left
        else:
            node = stack.pop()
            node = node.right
    return result

def preorder_short(node):
    stack, result = [node], []

    while stack:
        node = stack.pop()
        if node:
            result.append(node.data)
            stack += [node.right, node.left]

    return result