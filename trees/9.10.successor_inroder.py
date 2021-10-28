
# https://www.youtube.com/watch?v=5cPbNCrdotA
# time complexity is O(h)
def find_successor(node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    if not node:
        return None

    if node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    
    while node.parent and node.parent.right is node:
        node = node.parent
    
    return node.parent