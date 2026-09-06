class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        beg = 0
        winstat = 0
        res = float("-inf")
        for end in range(len(nums)):
            winstat += nums[end]
            if end-beg+1 == k:
                res = max(res, winstat)
                winstat -= nums[beg]
                beg += 1
        return res/k
