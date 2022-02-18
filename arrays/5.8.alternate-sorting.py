def rearrange(A: List[int]) -> None:
    for i in range(1, len(A), 2):
        if A[i-1] > A[i]:
            A[i-1], A[i] = A[i], A[i-1]
        if i+1 < len(A) and A[i+1] > A[i]:
           A[i+1], A[i] = A[i], A[i+1] 