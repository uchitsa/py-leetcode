class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        min1,min2 = float('inf'),float('inf')
        for n in nums[1:]:
            if n<min1:
                min2=min1
                min1=n
            elif n<min2:
                min2=n
        return nums[0]+min1+min2
