def shortest_equivalent_path(path: str) -> str:
    if not path:
        raise ValueError("empty path")
    
    stack = []

    processedPath = [path for path in path.split("/") if path not in (".", "")]
    for dir in processedPath:
        if dir == "..":
            if not stack or stack[-1] == "..":
                stack.append(dir)
            else:
                if stack[-1] == "/":
                    raise ValueError("path error")
                stack.pop()
        else:
            stack.append(dir)

    result = "/".join(stack)
    return "/"+result if path[0]=="/" else result