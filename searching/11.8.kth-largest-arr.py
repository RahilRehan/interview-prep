def find_kth_largest(k: int, A: List[int]) -> int:

    left, right = 0, len(A)-1

    def partition_around_pivot(left, right, pivot):
        pivotVal = A[pivot]
        newPivotIdx = left
        A[pivot], A[right] = A[right], A[pivot]
        for i in range(left, right):
            if A[i] > pivotVal:
                A[i], A[newPivotIdx] = A[newPivotIdx], A[i]
                newPivotIdx += 1
        A[right], A[newPivotIdx] = A[newPivotIdx], A[right]
        return newPivotIdx

    while left <= right:
        randomPivotPos = random.randint(left, right)
        sortedPivotPos = partition_around_pivot(left, right, randomPivotPos)
        if sortedPivotPos == k-1:
            return A[sortedPivotPos]
        elif sortedPivotPos < k-1:
            left = sortedPivotPos + 1    
        else:
            right = sortedPivotPos - 1 