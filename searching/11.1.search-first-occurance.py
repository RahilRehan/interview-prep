def search_first_of_k(A: List[int], k: int) -> int:

    if not A:
        return -1

    start, end = 0, len(A) - 1
    result = -1

    while start <= end:
        mid = start + (end-start)//2
        if k > A[mid]:
            start = mid + 1
        elif k < A[mid]:
            end = mid - 1
        else:
            result = mid
            end = mid - 1
    return result