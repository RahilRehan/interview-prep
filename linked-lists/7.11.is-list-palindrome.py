# t.c : O(n), s.c: O(1)
def is_linked_list_a_palindrome(L) -> bool:

    def reverse(node):
        prev = None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        return prev

    if not L or not L.next:
        return True

    slow = fast = L

    while fast and fast.next:
        slow, fast = slow.next, fast.next.next    
    
    revHead = reverse(slow)
    while revHead and L:
        if revHead.data != L.data:
            return False
        revHead, L = revHead.next, L.next
    
    return True