class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(c in "aieou" for c in s)
        
