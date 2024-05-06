def maxPower(s: str) -> int:
    maxlen = 0
    pre = None
    cur = 1
    for ch in s:
        if ch == pre:
            cur += 1
        else:
            cur = 1
            pre = ch
        maxlen = max(maxlen, cur)
    return maxlen


if __name__ == '__main__':
    print(maxPower("abbcccddddeeeeedcba"))
    print(maxPower("leetcode"))
