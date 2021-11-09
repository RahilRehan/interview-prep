def lca(node1: BinaryTreeNode,
        node2: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    
    path = set()

    while node1 or node2:
        if node1:
            if node1 in path:
                return node1
            path.add(node1)
            node1 = node1.parent

        if node2:
            if node2 in path:
                return node2
            path.add(node2)
            node2 = node2.parent
    return None