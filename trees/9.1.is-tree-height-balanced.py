def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    BalanceAndHeight = collections.namedtuple("BalanceAndHeight", ("isBalanced", "height"))

    def postOrder(node: BinaryTreeNode) -> BalanceAndHeight:

        if not node:
            return BalanceAndHeight(True, 0)
        if not node.left and not node.right:
            return BalanceAndHeight(True, 1)

        left = postOrder(node.left)
        right = postOrder(node.right)

        if not left.isBalanced or not right.isBalanced:
            return BalanceAndHeight(False, max(left.height, right.height))
        
        isBalanced = abs(left.height - right.height) <= 1
        return BalanceAndHeight(isBalanced, max(left.height, right.height)+1)

    return postOrder(tree).isBalanced