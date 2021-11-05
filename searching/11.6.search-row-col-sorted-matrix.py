def matrix_search(matrix: List[List[int]], x: int) -> bool:
    
    row, col = len(matrix)-1, 0

    while row > -1 and col < len(matrix[0]):
        current = matrix[row][col]
        if current == x:
            return True
        elif current < x:
            col += 1
        else:
            row -= 1
    
    return False