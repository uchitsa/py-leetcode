class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        prefs = [0]*n
        prefs[0] = nums[0]
        cnt = 0
        for i in range(1,n):
            prefs[i] = prefs[i-1]+nums[i]
        
        for i in range(n-1):
            if prefs[i] >= prefs[-1]-prefs[i]:
                cnt += 1

        return cnt
