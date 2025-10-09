class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        n = len(potions)
        maxi = potions[n-1]

        for sp in spells:
            mini = (success+sp-1)//sp
            if mini>maxi:
                res.append(0)
                continue
            idx = bisect.bisect_left(potions,mini)
            res.append(n-idx)
        return res
