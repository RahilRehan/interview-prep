def exterior_binary_tree(node: BinaryTreeNode) -> List[BinaryTreeNode]:
    
    def isLeaf(node):
        return not node.left and not node.right

    def leftBoundaryAndLeaves(node, isBoundary):
        if not node: return []

        return ([node] if isBoundary or isLeaf(node) else []) + \
            leftBoundaryAndLeaves(node.left, isBoundary) + \
            leftBoundaryAndLeaves(node.right, isBoundary and not node.left)

    def rightBoundaryAndLeaves(node, isBoundary):
        if not node: return []

        return rightBoundaryAndLeaves(node.left, isBoundary and not node.right) + \
            rightBoundaryAndLeaves(node.right, isBoundary) + \
            ([node] if isBoundary or isLeaf(node) else [])
    
    return ([node] + leftBoundaryAndLeaves(node.left, True) + rightBoundaryAndLeaves(node.right, True)) if node else []