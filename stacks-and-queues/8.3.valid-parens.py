def is_well_formed(s: str) -> bool:
    stack = []
    lookup = {"(": ")", "[" : "]", "{" : "}"}
    for c in s:
        if c in lookup:
            stack.append(c)
        elif len(stack) == 0 or c != lookup[stack.pop()]:
            return False
    return len(stack) == 0