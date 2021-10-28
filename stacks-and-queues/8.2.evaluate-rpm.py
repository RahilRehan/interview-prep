def evaluate(expression: str) -> int:
    stack = []
    for ele in expression.split(","):
        if ele.isnumeric():
            stack.append(ele)
        else:
            second = int(stack.pop())
            first = int(stack.pop())
            out = 0
            if ele == "+":
                out = first + second
            elif ele == "-":
                out = first - second
            elif ele == "*":
                out = first*second
            else:
                out = int(first/second)
            stack.append(str(out))
    return int(stack[-1])