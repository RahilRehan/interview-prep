def find_closest_k_stars(stars: Iterator[Star], k: int) -> List[Star]:
    result = []

    maxHeap = []

    for star in stars:
        heapq.heappush(maxHeap, (-star.distance, star))

        if len(maxHeap)>k:
            heapq.heappop(maxHeap)

    result = [s[1] for s in maxHeap]
    return result