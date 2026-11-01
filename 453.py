class Solution:
    def minMoves(self, nums: list[int]) -> int:
        cnt = 0
        mini = min(nums)
        for i in range(len(nums)):
            if nums[i] != mini:
                cnt += nums[i] - mini
        return cnt
