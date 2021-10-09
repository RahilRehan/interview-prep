def add_two_numbers(L1, L2):
    resultHead = resultTail = ListNode(0)
    carry = 0

    while L1 or L2 or carry!=0:
        addition = (L1.data if L1 else 0) + (L2.data if L2 else 0) + carry
        carry = addition//10    
        resultTail.next = ListNode(addition%10)
        L1 = L1.next if L1 else None
        L2 = L2.next if L2 else None
        resultTail = resultTail.next

    return resultHead.next