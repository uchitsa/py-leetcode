class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        maxi = 0
        for i in range(len(nums)):
            od = {}
            ev = {}
            for j in range(i,len(nums)):
                if nums[j] & 1:
                    od[nums[j]] = od.get(nums[j],0)+1
                else:
                    ev[nums[j]] = ev.get(nums[j],0)+1
                if len(od)==len(ev):
                    maxi = max(maxi, j-i+1)
        return maxi
