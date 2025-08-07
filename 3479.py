from collections import defaultdict
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        le = 0
        maxfru = 0
        bsk = defaultdict(int)
        for ri, fru in enumerate(fruits):
            bsk[fru] += 1
            while len(bsk)>3:
                lefru = fruits[le]
                bsk[lefru] -= 1
                if bsk[lefru] == 0:
                    del bsk[lefru]
                le += 1
            maxfru = max(maxfru, ri-le+1)
        return maxfru
