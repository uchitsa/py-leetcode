class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        cnt1, cnt2 = 0, 0
        for n in nums:
            if n < target:
                cnt1 += 1
            elif n == target:
                cnt2 += 1
        return list(range(cnt1, cnt1 + cnt2))
