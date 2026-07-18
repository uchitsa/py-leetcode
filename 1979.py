class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini = min(nums)
        maxi = max(nums)
        res = 0
        for i in range(1, mini+1):
            if maxi%i==0 and mini%i==0:
                res = i
        return res
