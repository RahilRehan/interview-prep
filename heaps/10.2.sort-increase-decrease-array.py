def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    sorted_arrays = []
    isIncreasing = True
    prevStartIdx = 0

    for i in range(len(A)):
        if (i == len(A)-1) or (A[i] > A[i+1] and isIncreasing) or (A[i] < A[i+1] and not isIncreasing):
            sorted_arrays.append(A[prevStartIdx:i+1] if isIncreasing else A[prevStartIdx:i+1][::-1])
            prevStartIdx = i+1
            isIncreasing = False if isIncreasing else True
    return merge_sorted_arrays(sorted_arrays)