class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        cnt, precnt, res = 1, 0, 0
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                cnt += 1
            else:
                precnt, cnt = cnt, 1
            res = max(res, min(precnt, cnt))
            res = max(res, cnt//2)
        return res >= k
