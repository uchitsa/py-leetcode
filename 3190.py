class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        for i in range(len(nums)):
            cnt += min(nums[i]%3, 3-(nums[i]%3))
        return cnt
