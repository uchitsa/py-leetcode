class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        x = 0
        for i in range(len(nums)):
            x = ((x<<1) + nums[i])%5
            res.append(x==0)
        return res
