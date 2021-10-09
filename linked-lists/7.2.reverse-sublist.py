def reverse_sublist(L, start, finish):
    if not L:
        return L
        
    dummy = subListPrev = ListNode(0, L)

    for _ in range(1, start):
        subListPrev = subListPrev.next

    subListHead = cur = subListPrev.next
    prev = None
    for _ in range(start, finish+1):
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    
    subListPrev.next = prev
    subListHead.next = cur
    
    return dummy.next