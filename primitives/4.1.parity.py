def parity(x):
    x = x ^ (x>>32)
    x = x ^ (x>>16)
    x = x ^ (x>>8)
    x = x ^ (x>>4)
    x = x ^ (x>>2)
    x = x ^ (x>>1)

    return x&1

def parity_remove_set_bit(x):
    result = 0

    while x:
        result = result ^ 1
        x = x&(x-1)

    return result

def parity_brute(x: int) -> int:
    result = 0
    while x:
        result = result ^ x&1
        x = x >> 1
    return result