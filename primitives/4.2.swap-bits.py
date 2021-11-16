def swap_bits(x, i, j):
    if (x >> i)&1 != (x >> j)&1:  # swap bits only if bits at i and j index are different
        bitMask = (1 << i) | (1 << j) # create a mask with i and j bits set
        x ^= bitMask # if bit at index is 0 => (0^1)=1. If it is 1 => (1^1) = 0
    return x