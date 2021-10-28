def create_list_of_leaves(node: BinaryTreeNode) -> List[BinaryTreeNode]:

    if not node:
        return []
    if not node.left and not node.right:
        return [node]
    return create_list_of_leaves(node.left) + create_list_of_leaves(node.right)