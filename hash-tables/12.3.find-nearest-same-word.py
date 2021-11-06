def find_nearest_repetition(paragraph: List[str]) -> int:
    minDist = float('inf')
    prevSeen = dict()

    for idx, word in enumerate(paragraph):
        if word in prevSeen:
            minDist = min(minDist, idx - prevSeen[word])
        prevSeen[word] = idx

    return -1 if minDist == float("inf") else minDist