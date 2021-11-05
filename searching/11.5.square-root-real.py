def square_root(x: float) -> float:
    # if given number is proper fraction, then answer lies between (fraction and 1.0)
    # if number greater than or equal to one, number lies between (1 and given number)
    left, right = (x, 1.0) if x < 1.0 else (1.0, x)
    
    # perform a binary search to find the square root
    while not math.isclose(left, right): # iterate until left and right are almost equal
        mid = 0.5*(left + right)
        square = mid*mid
        if square < x:
            left = mid
        else:
            right = mid
    return right #can also return left