def reconstruct_preorder(preorder: List[int]) -> BinaryTreeNode:
    dq = deque(preorder)

    def buildTree():
        x = dq.popleft()
        if not x: return x
        node = BinaryTreeNode(x)
        node.left = buildTree()
        node.right = buildTree()
        return node

    return buildTree()