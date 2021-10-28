def construct_right_sibling(tree: BinaryTreeNode) -> None:
    levelHash = {}

    def setNext(node, level):
        if not node: return
        if level in levelHash:
            levelHash[level].next = node
        levelHash[level] = node
        setNext(node.left, level + 1)
        setNext(node.right, level + 1)

    setNext(tree, 0)