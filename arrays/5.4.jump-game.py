def can_reach_end(A: List[int]) -> bool:
    farthestReachSoFar = 0
    needToReach = len(A)-1

    i = 0
    while i <= farthestReachSoFar and farthestReachSoFar < needToReach:
        farthestReachSoFar = max(farthestReachSoFar, A[i]+i)
        i += 1
    return farthestReachSoFar >= needToReach

def can_reach_end_simple(A): # own easy solution, traverse from back
    needToReach = len(A)-1

    for i in reversed(range(len(A))):
        if i + A[i] >= needToReach:
            needToReach = i
    return needToReach == 0