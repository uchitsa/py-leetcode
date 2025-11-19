class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nset = set(nums)
        while original in nset:
            original *= 2
        return original
