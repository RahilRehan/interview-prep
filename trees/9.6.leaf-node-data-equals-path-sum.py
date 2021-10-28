def has_path_sum(node: BinaryTreeNode, remaining_weight: int) -> bool:
    if not node:
        return False
        
    if not node.left and not node.right:
        return remaining_weight == node.data

    return has_path_sum(node.left, remaining_weight-node.data) or \
        has_path_sum(node.right, remaining_weight-node.data)