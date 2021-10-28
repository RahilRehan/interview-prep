def is_symmetric(node: BinaryTreeNode) -> bool:
    def check_symmetry(node1, node2):
        if not node1 and not node2:
            return True
        
        if node1 and node2:
            return \
                node1.data == node2.data and\
                check_symmetry(node1.left, node2.right) and\
                check_symmetry(node1.right, node2.left)
        
        return False
    
    return not node or check_symmetry(node.left, node.right)