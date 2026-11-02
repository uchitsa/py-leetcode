class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        return sum(abs(a - b) for a, b in zip(sorted(nums), sorted(nums)[::-1])) // 2
