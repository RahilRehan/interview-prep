def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    start = 0
    seen = defaultdict(int)
    smallestCover = Subarray(0, len(paragraph)-1)

    for end, word in enumerate(paragraph):
        if word in keywords:
            seen[word] += 1
            while len(seen) >= len(keywords):
                if end-start+1 < smallestCover.end-smallestCover.start+1:
                    smallestCover = Subarray(start, end) 
                startWord = paragraph[start]
                if startWord in seen:
                    seen[startWord] -= 1
                    if seen[startWord] == 0:
                        del seen[startWord]
                start += 1 
    return smallestCover

# time complexity => O(N). visiting each element twice
# space complexity => O(K). where K is length of keywords