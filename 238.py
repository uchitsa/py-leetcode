class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        le, ri = [1]*n, [1]*n
        res = [0]*n
        for i in range(1,n):
            le[i] = nums[i-1]*le[i-1]
        for i in reversed(range(n-1)):
            ri[i] = nums[i+1]*ri[i+1]
        for i in range(n): 
            res[i] = le[i]*ri[i]
        return res
