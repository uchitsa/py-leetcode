class Solution:
    def minimumSum2(self, grid: List[List[int]],u:int,d:int,l:int,r:int) -> int:
        mini, minj = len(grid), len(grid[0])
        maxi, maxj = 0, 0
        for i in range(u,d+1):
            for j in range(l,r+1):
                if grid[i][j] == 1:
                    mini = min(mini, i)
                    minj = min(minj, j)
                    maxi = max(maxi, i)
                    maxj = max(maxj, j)
        return (maxi-mini+1)*(maxj-minj+1) if mini <= maxi else sys.maxsize//3
    
    def rot(self, arr):
        n = len(arr)
        m = len(arr[0]) if n > 0 else 0
        res = [[0]*n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                res[m-j-1][i] = arr[i][j]
        return res

    def slv(self, grid):
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0
        res = n*m
        for i in range(n-1):
            for j in range(m-1):
                res = min(res,self.minimumSum2(grid,0,i,0,m-1)+self.minimumSum2(grid,i+1,n-1,0,j)+self.minimumSum2(grid,i+1,n-1,j+1,m-1))
                res = min(res,self.minimumSum2(grid,0,i,0,j)+self.minimumSum2(grid,0,i,j+1,m-1)+self.minimumSum2(grid,i+1,n-1,0,m-1))
        for i in range(n-2):
            for j in range(i+1,n-1):
                res = min(res,self.minimumSum2(grid,0,i,0,m-1)+self.minimumSum2(grid,i+1,j,0,m-1)+self.minimumSum2(grid,j+1,n-1,0,m-1))
        return res

    def minimumSum(self, grid):
        rgri = self.rot(grid)
        return min(self.slv(grid),self.slv(rgri))
    
