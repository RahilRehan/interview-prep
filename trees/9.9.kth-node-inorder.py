# time complexity is O(h)
def find_kth_node_binary_tree(node: BinaryTreeNode,
                              k: int) -> Optional[BinaryTreeNode]:
    while node:
        left_size = node.left.size if node.left else 0
        if k > left_size + 1:
            k -= (left_size + 1)
            node = node.right
        elif k == left_size + 1:
            return node
        else:
            node = node.left
    
    return None


# time complexity is O(N)
def find_kth_node_binary_tree_extra_space(node: BinaryTreeNode,
                              k: int) -> Optional[BinaryTreeNode]:
    count = [0]

    def kthNode(node):
        if node:
            l = kthNode(node.left)
            count[0] += 1
            if count[0] == k:
                return node
            r = kthNode(node.right)
            return l if l else r

    return kthNode(node)