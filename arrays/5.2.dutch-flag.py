def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    pivot = A[pivot_index]

    small, equal, large = 0, 0, len(A)-1

    while equal <= large:

        if A[equal] < pivot:
            A[small], A[equal] = A[equal], A[small]
            small += 1
            equal += 1
        elif A[equal] > pivot:
            A[large], A[equal] = A[equal], A[large]
            large -= 1
        else:
            equal += 1