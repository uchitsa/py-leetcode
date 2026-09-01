class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        res = 0
        prefs = 0
        for n in nums:
            prefs += n
            res = min(prefs,res)
        return -res+1
