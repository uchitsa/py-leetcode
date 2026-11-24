class Solution:
    def maxLength(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            prodval = nums[i]
            gcdval = nums[i]
            lcmval = nums[i]
            for j in range(i + 1, len(nums)):
                prodval = prodval * nums[j]
                gcdval = gcd(gcdval, nums[j])
                lcmval = lcm(lcmval, nums[j])
                if prodval > gcdval * lcmval:
                    break
                if prodval == gcdval * lcmval:
                    res = max(res, j - i + 1)
        return res
