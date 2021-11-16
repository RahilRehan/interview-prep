# if given 64 bit integer
# and you even have to reverse the bits before highest set bit. ex: 110 becomes 01100000...(61 zeros)
# swap bits
def reverse_bits(x: int) -> int:
    start, end = 0, 63
    while start < end:
        if (x >> start)&1 != (x >> end)&1:
            bitMask = (1 << start) | (1 << end)
            x ^= bitMask    
        start += 1
        end -= 1
    return x


# and you dont have to reverse the bits before highest set bit. ex: 110 becomes 011
def reverseBits(n) :
    rev = 0
    while (n > 0) :
        rev = rev << 1
        if (n & 1 == 1) :
            rev = rev ^ 1
        n = n >> 1
    return rev

# there is solution using caching