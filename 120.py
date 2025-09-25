class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for r in range(1,len(triangle)):
            for c in range(r+1):
                smalle = math.inf
                if c>0:
                    smalle = triangle[r-1][c-1]
                if c<r:
                    smalle = min(smalle,triangle[r-1][c])
                triangle[r][c] += smalle
        return min(triangle[-1])
