class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt = 0
        pre = -math.inf
        for n in nums:
            cur =  min(max(n-k,pre+1),n+k)
            if cur>pre:
                cnt += 1
                pre = cur
        return cnt
