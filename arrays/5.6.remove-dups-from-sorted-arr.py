def delete_duplicates(A: List[int]) -> int:
    n = len(A)

    if n == 0 or n == 1:
        return len(A)

    # unique index
    j = 0

    for i in range(len(A)-1):
        if A[i]!=A[i+1]:
            A[i], A[j] = A[j], A[i]
            j += 1
    
    A[j] = A[n-1]
    j += 1

    return j