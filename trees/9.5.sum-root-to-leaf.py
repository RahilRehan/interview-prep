def sum_root_to_leaf(tree: BinaryTreeNode, pathSum = 0, power=0) -> int:
    if not tree:
        return 0

    pathSum += tree.data*(2**power)
    
    if not tree.left and not tree.right:
        return pathSum
    
    return sum_root_to_leaf(tree.left, pathSum, power+1) + sum_root_to_leaf(tree.right, pathSum, power+1)