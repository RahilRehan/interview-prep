def longest_contained_range(A: List[int]) -> int:
    unprocessedElements = set(A)
    maxLength = 0

    while unprocessedElements:
        ele = unprocessedElements.pop()

        lowerBound = ele-1
        while lowerBound in unprocessedElements:
            unprocessedElements.remove(lowerBound)
            lowerBound -= 1

        upperBound = ele+1
        while upperBound in unprocessedElements:
            unprocessedElements.remove(upperBound)
            upperBound += 1
        
        maxLength = max(maxLength, upperBound-lowerBound-1)

    return maxLength