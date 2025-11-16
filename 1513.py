class Solution:
    def numSub(self, s: str) -> int:
        total = 0
        cons = 0
        for i in range(len(s)):
            if s[i]=='0':
                total += cons*(cons+1)//2
                cons = 0
            else:
                cons += 1
        total += cons*(cons+1)//2
        total %= 10**9+7
        return total
