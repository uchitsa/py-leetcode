class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        maxpart = 0
        for c in candies:
            maxpart = max(maxpart, c)
        le = 0
        ri = maxpart
        while le<ri:
            mi = (le+ri+1)//2
            if self.can_alloc(candies,k,mi):
                le = mi
            else:
                ri = mi - 1
        return le

    def can_alloc(self, candies, k, numcandies):
        maxi = 0
        for c in candies:
            maxi += c // numcandies
        return maxi >= k
