def count_bits(x: int) -> int:
    count = 0
    while x:
        count += 1
        x = x&(x-1)
    return count