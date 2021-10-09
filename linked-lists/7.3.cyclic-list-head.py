def has_cycle_1(head):

    def getListLength(end):
        start = end
        length = 0
        while True:
            length += 1
            start = start.next
            if start is end:
                return length

    slow = fast = head
    while slow and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            start = end = head
            for _ in range(getListLength(slow)):
                end = end.next
            while start is not end:
                start = start.next
                end = end.next
            return start
    
    return None

# this works! for proof https://www.youtube.com/watch?v=-YiQZi3mLq0
# if you solve the question this way, you also need to provide proof
def has_cycle_2(head):
    slow = fast = head
    while slow and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            slow = head
            while slow is not fast:
                slow, fast = slow.next, fast.next
            return slow
    return None