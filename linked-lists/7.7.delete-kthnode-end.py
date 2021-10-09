# delete kth node from end and return head

def remove_kth_last(L, k):
    slow = fast = L

    # move fast node k nodes ahead
    for _ in range(k):
        fast = fast.next
    
    # if it is first node that is to be deleted, fast node will have exhausted
    if fast == None:
        L = L.next
        return L

    # move slow node just before the node to be deleted
    while fast.next:
        fast = fast.next
        slow = slow.next

    # deletion of node
    slow.next = slow.next.next

    return L