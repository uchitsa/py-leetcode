from collections import Counter
class Solution:
    def maxFreqSum(self, s: str) -> int:
        m = Counter(s)
        vow = max((m[c] for c in m if c in 'aieou'), default=0)
        cons =max((m[c] for c in m if c not in 'aieou'), default=0)
        return vow+cons
        
