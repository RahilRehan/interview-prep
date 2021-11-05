def search_entry_equal_to_its_index(A: List[int]) -> int:

    start, end = 0, len(A)-1

    while start <= end:
        mid = start + (end-start)//2
        difference = A[mid] - mid
        if difference == 0:
            return mid
        elif difference < 0:
            start = mid + 1
        else:
            end = mid - 1
    return -1