def parseBoolExpr(expression: str) -> bool:
    op_stack = []
    args_stack = []

    for c in expression:
        if c in "!&|":
            op_stack.append(c)
        elif c == "t":
            args_stack.append(True)
        elif c == "f":
            args_stack.append(False)
        elif c == "(":
            args_stack.append(c)
        elif c == ")":
            res = args_stack.pop()
            op = op_stack.pop()
            if op == "!":
                res = not res
            else:
                while args_stack[-1] != "(":
                    if op == "|":
                        res |= args_stack.pop()
                    else:
                        res &= args_stack.pop()
            args_stack.pop()
            args_stack.append(res)

    return args_stack.pop()


if __name__ == '__main__':
    print(parseBoolExpr("&(|(f))"))
    print(parseBoolExpr("|(f,f,f,t)"))
    print(parseBoolExpr("!(&(f,t))"))
