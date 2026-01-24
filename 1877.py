class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        smax = 0
        for i in range(0, int(len(nums)/2)):
            smax = max(smax, nums[i]+nums[len(nums)-i-1])
        return smax
