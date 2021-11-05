def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:

    minHeap = []
    result = []

    iters = [iter(arr) for arr in sorted_arrays]

    for iterIdx, it in enumerate(iters):
        number = next(it, None)
        if number is not None:
            heapq.heappush(minHeap, (number, iterIdx))
    
    while minHeap:
        number, iterIdx = heapq.heappop(minHeap)    
        result.append(number)
        nextIter = iters[iterIdx]
        nextNumber = next(nextIter, None)
        if nextNumber is not None:
            heapq.heappush(minHeap, (nextNumber, iterIdx))

    return result

# time complexity: logk for insertion and deletion of min element, total O(nlogk), where n is total number of elements
# space complexity: O(logk) for heap