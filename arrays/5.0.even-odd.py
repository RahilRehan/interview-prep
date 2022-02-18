def even_odd(A: List[int]) -> None:
    start, end = 0, len(A)-1
    while start < end:
        if not A[start]&1: # if start is even
            start += 1
        else:
            A[start], A[end] = A[end], A[start]
            end -= 1