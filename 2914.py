class Solution:
    def minChanges(self, s: str) -> int:
        cur = s[0]
        conscnt = 0
        minchg = 0
        for c in s:
            if c == cur:
                conscnt += 1
                continue
            if conscnt % 2 == 0:
                conscnt = 1
            else:
                conscnt = 0
                minchg += 1
            cur = c
        return minchg
