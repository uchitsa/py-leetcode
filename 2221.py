class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums)>1:
            neos = []
            for i in range(len(nums)-1):
                neos.append((nums[i]+nums[i+1])%10)
            nums = neos
        return nums[0]
