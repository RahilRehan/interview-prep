def search_smallest(A: List[int]) -> int:
    start, end = 0, len(A)-1
    while start < end:
        mid = start + (end-start)//2
        if A[mid] < A[end]:
            end = mid
        else:
            start = mid + 1
    return end