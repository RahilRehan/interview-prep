def closest_int_same_bit_count(x: int) -> int:
    NUM_BITS = 64

    for i in range(NUM_BITS - 1):
        if (x >> i) &1 != (x >> (i+1)) & 1:
            x ^= (1 << i) | (1 << (i+1))
            return x
    
    raise ValueError("All bits are 0 or 1")