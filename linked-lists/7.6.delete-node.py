# Assume given node is not tail
# t.c O(1), s.c O(1)
def deletion_from_list(node_to_delete):
    node_to_delete.data = node_to_delete.next.data
    node_to_delete.next = node_to_delete.next.next
    return node_to_delete