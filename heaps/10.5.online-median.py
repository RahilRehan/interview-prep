def online_median(sequence: Iterator[int]) -> List[float]:
    # good example: [1, 0, 3, 5, 2, 0, 1]
    # minheap stores the larger half of array
    # maxheap stores the smaller half of array
    minHeap, maxHeap = [], []
    result = []

    for x in sequence:
        # first insert element into minheap then get minimum element from minheap and push it onto maxheap
        heapq.heappush(maxHeap, -heapq.heappushpop(minHeap, x))

        # make sure, minheap and max heap have equal number of elements or minheap contains one element more than maxheap
        if len(maxHeap) > len(minHeap):
            heapq.heappush(minHeap, -heapq.heappop(maxHeap))

        median = 0.5*((-maxHeap[0])+minHeap[0]) if len(minHeap) == len(maxHeap) else minHeap[0]
        result.append(median)

    return result
