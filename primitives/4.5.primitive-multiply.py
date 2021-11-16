# https://www.youtube.com/watch?v=WfWHdWwITgk
def multiply(x: int, y: int) -> int:
    def add(a, b):
        running_sum, carry_in, k, temp_a, temp_b = 0, 0, 1, a, b
        carry_out = 0
        while temp_a or temp_b:
            ak, bk = a&k, b&k
            carry_out = (ak & bk) | (ak & carry_in) | (bk & carry_in)
            running_sum |= (ak ^ bk ^ carry_in)
            carry_in, k, temp_a, temp_b = (carry_out<<1, k<<1, temp_a>>1, temp_b>>1)
        
        return running_sum | carry_in


    runningSum = 0
    while x:
        if x&1:
            runningSum = add(runningSum, y)
        # remove LSB in x, shift y to get pow(2, k)
        x, y = x >> 1, y << 1
    return runningSum