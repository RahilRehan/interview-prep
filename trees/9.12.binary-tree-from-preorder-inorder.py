def binary_tree_from_preorder_inorder(preorder: List[int],
                                      inorder: List[int]) -> BinaryTreeNode:

    map_inorder = {}
    preorder = deque(preorder)
    for i, val in enumerate(inorder): map_inorder[val] = i

    def buildTree(start, end):
        if start > end: return None
        x = BinaryTreeNode(preorder.popleft())
        index = map_inorder[x.data]
        x.left = buildTree(start, index-1)
        x.right = buildTree(index+1, end)
        return x
    return buildTree(0, len(inorder)-1)
