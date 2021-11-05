MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A: List[int]) -> MinMax:
    
    def min_max(a, b):
        return MinMax(a, b) if a < b else MinMax(b, a)

    if not A:
        return None
    
    if len(A) == 1:
        return MinMax(A[0], A[0])
    
    globalMinMax = min_max(A[0], A[1])

    for idx in range(2, len(A)-1, 2):
        localMinMax = min_max(A[idx], A[idx+1])
        globalMinMax = MinMax(min(globalMinMax.smallest, localMinMax.smallest), max(globalMinMax.largest, localMinMax.largest))

    if len(A)&1: # array is odd length
        globalMinMax = MinMax(min(globalMinMax.smallest, A[-1]), max(globalMinMax.largest, A[-1]))

    return globalMinMax

# in bruteforce, finind min and max takes O(2*(n-1)) time
# when u do comparisions in pairs the time complexity is brought down to O(3*n/2 - 2)
# breakdown of t.c => 
# as we compare in pairs we have n/2 pairs
# for each pair, we perform three operations
# 1. compare with each other to find local min and max => 1 operation
# 2. compare local min and max with global min and max => 2 operations
# so total => 3*(n/2)
# but we do not have local min and max for first two indices
# hence, t.c becomes 3*(n/2)-2
