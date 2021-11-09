def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    start = 0
    maxLength = 0
    seen = defaultdict(int)

    for end in range(len(A)):
        while A[end] in seen:
            if A[start] in seen:
                seen[A[start]] -= 1
                if seen[A[start]] == 0:
                    del seen[A[start]]
            start += 1
        seen[A[end]] += 1
        maxLength = max(maxLength, end-start+1)
    return maxLength