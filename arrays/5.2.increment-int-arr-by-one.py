def plus_one(A: List[int]) -> List[int]:
    if not A:
        return
    
    A[-1] += 1

    for i in reversed(range(1, len(A))):
        if A[i] == 10:
            A[i-1] += 1
            A[i] = 0

    if A[0] == 10:
        A.append(0)
        A[0] = 1

    return A