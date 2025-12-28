class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0
        m = len(grid[0])
        n = len(grid)
        for i in range(n):
            for j in range(m):
                if grid[i][j]<0:
                    cnt += 1
        return cnt
