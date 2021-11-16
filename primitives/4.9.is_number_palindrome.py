# reverse function from 4.8 problem
def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return x == 0

    return x == reverse(x)