# time complexity: O(N) as each node is just visited once
# space complexity: O(1), we are using 5 variables thats it

def even_odd_merge(L):

    if not L:
        return L

    evenHead, oddHead = ListNode(0), ListNode(0)
    evenTail, oddTail = evenHead, oddHead
    turn = 0

    while L:
        if turn == 0:
            evenTail.next = L
            evenTail = evenTail.next
        else:
            oddTail.next = L
            oddTail = oddTail.next
        turn ^= 1
        L = L.next
    
    oddTail.next = None
    evenTail.next = oddHead.next

    return evenHead.next