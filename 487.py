class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        maxi = 0
        zeros = 0
        l, r = 0, 0
        while r < len(nums):
            if nums[r] == 0:
                zeros += 1
            while zeros == 2:
                if nums[l] == 0:
                    zeros -= 1
                l += 1
            maxi = max(maxi, r - l + 1)
            r += 1
        return maxi

