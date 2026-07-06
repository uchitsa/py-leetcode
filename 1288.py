class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0],-x[1]))
        res = 0
        pre = -inf
        for _, cur in intervals:
            if cur > pre:
                res += 1
                pre = cur
        return res
        
