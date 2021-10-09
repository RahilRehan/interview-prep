def overlapping_no_cycle_lists_hashmap(l0, l1):
    hashmap = set()
    while l0:
        hashmap.add(l0)
        l0 = l0.next
    while l1:
        if l1 in hashmap:
            return l1
        l1 = l1.next
    return None

def overlapping_no_cycle_lists(l0, l1):

    # find length of two lists => m, n 
    # move longest list m-n times so that they have same length
    # move both longest and shortest list in tandem to get to meeting point

    def findLength(head):
        length = 0
        while head:
            head = head.next
            length += 1
        return length

    m = findLength(l0)
    n = findLength(l1)

    if m > n:
        longest = l0
        shortest = l1
    else:
        longest = l1
        shortest = l0
    
    for _ in range(abs(m-n)):
        longest = longest.next
    
    while longest and shortest and longest is not shortest:
        longest = longest.next
        shortest = shortest.next
    
    return shortest