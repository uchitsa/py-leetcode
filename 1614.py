class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        st = []
        for c in s:
            if c == '(':
                st.append(c)
            elif c == ')' and st:
                st.pop()
            res = max(res, len(st))
        return res
