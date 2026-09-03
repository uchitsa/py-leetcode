class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        m = nums1[0]
        odds = False
        for n in nums1:
            if n < m:
                m = n
            if n%2==1:
                odds = True
        if m%2==1:
            return True
        return not odds
