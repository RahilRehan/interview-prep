# move node which has greater depth to the same depth as other node
# once both of the nodes are at same level, just traverse until you meet lca
# getting depth is trivial as we have parent node
def lca(node1: BinaryTreeNode,
        node2: BinaryTreeNode) -> Optional[BinaryTreeNode]:

    def getDepth(node: BinaryTreeNode):
        depth = 0
        while node:
            depth += 1
            node = node.parent
        return depth
    
    d1, d2 = getDepth(node1), getDepth(node2)

    # store greater depth node in d1
    if d2 > d1:
        node1, node2 = node2, node1
    
    diff = abs(d1-d2)

    while diff:
        node1 = node1.parent
        diff -= 1

    while node1 and node2:
        if node1 == node2:
            return node1
        node1 = node1.parent
        node2 = node2.parent


def lcaHash(node1: BinaryTreeNode,
        node2: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    if not node1 and not node2:
        return None
    
    if not node1:
        return node2
    
    if not node2:
        return node1

    if node1 == node2:
        return node1
    
    hashmap = set()

    while node2:
        hashmap.add(node2)
        node2 = node2.parent
    
    while node1:
        if node1 in hashmap:
            return node1
        node1 = node1.parent