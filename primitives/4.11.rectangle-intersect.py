def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    def isIntersect(r1, r2):
        return (r1.x <= r2.x+r2.width) and (r2.x <= r1.x+r1.width) and \
            (r1.y <= r2.y+r2.height) and (r2.y <= r1.y+r1.height)

    if not isIntersect(r1, r2):
        return Rect(0, 0, -1, -1)

    return Rect(
        max(r1.x, r2.x),
        max(r1.y, r2.y),
        min(r1.x + r1.width, r2.x + r2.width) - max(r1.x, r2.x),
        min(r1.y + r1.height, r2.y + r2.height) - max(r1.y, r2.y)
    )