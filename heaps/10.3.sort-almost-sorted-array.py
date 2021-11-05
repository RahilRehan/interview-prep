def sort_approximately_sorted_array_pythonic(sequence: Iterator[int],
                                    k: int) -> List[int]: 
    result = []
    minHeap = []

    for x in itertools.islice(sequence, k):
        heapq.heappush(minHeap, x)
    
    for x in sequence:
        result.append(heapq.heappushpop(minHeap, x))
    
    while minHeap:
        result.append(heapq.heappop(minHeap))

    return result

    
def sort_approximately_sorted_array_mine(sequence: Iterator[int],
                                    k: int) -> List[int]:
    heap = []
    result = []

    counter = 0
    
    while True:
        nextEle = next(sequence, None)
        if nextEle is None:
            break
        if counter < k:
            heapq.heappush(heap, nextEle)
            counter += 1
        else:
            result.append(heapq.heappushpop(heap, nextEle))
    while heap:
        result.append(heapq.heappop(heap))
    return result
    