def square_root(k: int) -> int:
    start = 0
    end = k

    while start <= end:
        mid = start + (end-start)//2
        square = mid * mid
        if square <= k:
            start = mid + 1
        else:
            end = mid - 1
    return start-1