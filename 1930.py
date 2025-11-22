class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        st = set(s)
        res = 0
        for c in st:
            i, j = s.index(c), s.rindex(c)
            mid = set()
            for k in range(i+1,j):
                mid.add(s[k])
            res += len(mid)
        return res
        
