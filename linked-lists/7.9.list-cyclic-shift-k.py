# time complexity => O(N)
# space complexity => O(1)
def cyclically_right_shift_list(L, k):

    if not L:
        return None

    tail, N = L, 1
    while tail.next:
        tail = tail.next
        N += 1

    k = k%N
    if k == 0:
        return L

    # make list cyclic
    tail.next = L    

    # move tail, just before new head node
    for _ in range(N-k):
        tail = tail.next

    # set new head and disconnect tail
    L = tail.next
    tail.next = None

    return L      