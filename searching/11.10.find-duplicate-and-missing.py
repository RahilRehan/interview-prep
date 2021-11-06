# cyclic sort approach => O(N) time, two passes
def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:

    for idx in range(len(A)):
        while A[idx] != idx and A[A[idx]]!=A[idx]:
            A[A[idx]], A[idx] =A[idx], A[A[idx]]

    for idx in range(len(A)):
        if idx != A[idx]:
            return DuplicateAndMissing(A[idx], idx)