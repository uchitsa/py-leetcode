def isValid(s: str) -> bool:
    stack = []
    config = {")": "(", "]": "[", "}": "{"}
    for c in s:
        if c == "(" or c == "[" or c == "{":
            stack.append(c)
            continue
        if len(stack) == 0:
            return False
        if stack.pop() != config[c]:
            return False
    return len(stack) == 0


if __name__ == '__main__':
    print(isValid("()"))
    print(isValid("()[]{}"))
    print(isValid("(]"))
