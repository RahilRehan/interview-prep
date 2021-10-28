def inorder_traversal(node: BinaryTreeNode) -> List[int]:
    # node => parent
    # inorder => visit left subtree, visit the current node, visit the left subtree

    prev, result = None, []

    while node:
        if node.parent == prev: # we are coming down from parent node
            if node.left: # if left node exist, explore it first
                next = node.left
            else: # no left nodes, visit this node and explore right subtree. But if no right subtree go back to parent
                result.append(node.data)
                next = node.right or node.parent

        elif node.left == prev: # if done exploring left subtree, and we are back to parent
            result.append(node.data) # visit node as left subtree is completed
            next = node.right or node.parent # visit right subtree if exist or visit parent

        else: # if done visiting right subtree as well 
            next = node.parent

        prev, node = node, next
    
    return result