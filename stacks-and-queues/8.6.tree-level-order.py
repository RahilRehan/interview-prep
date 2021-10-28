# t.c => O(N), s.c => O(m) maximum number of nodes in a given level
def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    if not tree:
        return []

    q = collections.deque([tree])
    result = []
    while len(q):
        result.append([ele.data for ele in q])
        q = [child 
                for ele in q 
                for child in 
                    (ele.left, ele.right)
                if child
            ]
    return result