def reverse(x: int) -> int:
    neg = True if x < 0 else False
    x, rev = abs(x), 0
    while x:
        rev = (rev*10)+(x%10)
        x //= 10
    return -rev if neg else rev