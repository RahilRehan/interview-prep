def lca(node: BinaryTreeNode, node1: BinaryTreeNode,
        node2: BinaryTreeNode) -> Optional[BinaryTreeNode]:

    if not node:
        return None
    
    if node is node1 or node is node2:
        return node

    l = lca(node.left, node1, node2)
    r = lca(node.right, node1, node2)

    if not l and not r:
        return None
    
    if l and r:
        return node
    
    return l if l else r