# T.C => O(m + n), S.C is O(1)

def overlapping_lists(l1,l2):
    # has_cycle returns the start of the cycle
    # overlapping_no_cycle_lists returns the intersection of linked lists(no cycles are present)

    c1, c2 = has_cycle(l1), has_cycle(l2)

    # if both lists do no have cycle, then they can overlap without a cycle
    if not c1 and not c2:
        return overlapping_no_cycle_lists(l1, l2)
    # if one list has cycle and other doesn't. They never overlap
    elif (not c1 and c2) or (c1 and not c2):
        return None

    # both lists have cycle
    # case: cycles can still be disjoin(i.e they still do not overlap)
    temp = c1
    while True:
        temp = temp.next
        if temp is c2 or temp is c1:
            break
    # list are disjoint, we did not meet the other cycle head
    if temp is not c2:
        return None

    def distance(a, b):
        dis = 0
        while a is not b:
            a = a.next
            dis += 1
        return dis

    # calculate distances to cycles
    stemLen1, stemLen2 = distance(l1, c1), distance(l2, c2)

    # make l1 as the shortest list (i.e distance between l1 and c1 is less than l2 and c2)
    if stemLen1 > stemLen2:
        l1, l2 = l2, l1
        c1, c2 = c2, c1
    
    # move l2 abs diff of stemLen1 - stemLen2
    for _ in range(abs(stemLen2 - stemLen1)):
        l2 = l2.next
    
    # two cases
    # case 1: overlap before cycle
    # case 2: overlap after cycle

    while l1 is not l2 and l1 is not c1 and l2 is not c2:
        l1, l2 = l1.next, l2.next

    # if l1 is l2, then they overlap before cycle
    # else they overlap after cycle, and we can return any node in cycle 
    return l1 if l1 is l2 else c1