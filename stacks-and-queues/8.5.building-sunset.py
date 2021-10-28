# t.c => O(N) and s.c => O(N) worst case
def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    stack = []
    for idx, ht in enumerate(sequence):
        while stack and ht >= stack[-1][0]:
            stack.pop()
        stack.append((ht, idx))
    return [idx for _, idx in reversed(stack)]