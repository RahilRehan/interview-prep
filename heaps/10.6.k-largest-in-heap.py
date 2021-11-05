def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    result = []
    maxHeap = []

    heapq.heappush(maxHeap, (-A[0], 0))

    for _ in range(k):
        largest = heapq.heappop(maxHeap)
        result.append(-largest[0])

        leftChildIdx = 2 * largest[1] + 1
        rightChildIdx = 2 * largest[1] + 2

        if leftChildIdx < len(A):
            heapq.heappush(maxHeap, (-A[leftChildIdx], leftChildIdx))
        if rightChildIdx < len(A):
            heapq.heappush(maxHeap, (-A[rightChildIdx], rightChildIdx))

    return result