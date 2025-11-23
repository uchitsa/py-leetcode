class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        f = [0, -float('inf'),-float('inf')]
        for n in nums:
            g = f[:]
            for i in range(3):
                g[(i+n%3)%3] = max(g[(i+n%3)%3], f[i]+n)
            f = g
        return f[0]
        
