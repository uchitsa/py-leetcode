class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefs = 0
        for i in range(len(nums)):
            if total - prefs - nums[i] == prefs:
                return i
            prefs += nums[i]

        return -1
      
