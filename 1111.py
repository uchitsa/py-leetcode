class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []
        cur = 0
        for c in seq:
            if c == '(':
                cur += 1
                res.append(cur % 2)
            elif c == ')':
                res.append(cur % 2)
                cur -= 1
        return res
