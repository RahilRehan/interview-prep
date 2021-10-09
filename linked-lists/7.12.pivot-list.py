def list_pivoting(l,x):
    smallerHead = smallerTail  = ListNode(0)
    greaterHead = greaterTail = ListNode(0)
    equalHead = equalTail = ListNode(0)

    while l:
        if l.data < x:
            smallerTail.next = l
            smallerTail = smallerTail.next
        elif l.data > x:
            greaterTail.next = l
            greaterTail = greaterTail.next
        else:
            equalTail.next = l
            equalTail = equalTail.next
        l = l.next
    
    # merge
    greaterTail.next = None
    equalTail.next = greaterHead.next
    smallerTail.next = equalHead.next
