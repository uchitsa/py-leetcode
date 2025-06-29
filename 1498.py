class Solution:
    import bisect
    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        mo = 10**9+7
        n = len(nums)
        nums.sort()
        for le in range(n):
            ri = bisect.bisect_right(nums, target-nums[le])-1
            if le <= ri:
                res += pow(2, ri-le, mo)
        return res % mo
        
