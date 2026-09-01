class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefs = 0
        res = 0
        for h in gain:
            prefs += h
            res = max(res, prefs)
        return res
