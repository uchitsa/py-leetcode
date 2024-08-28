def countSubIslands(grid1: List[List[int]], grid2: List[List[int]]) -> int:
    def dfs(x,y):
        if x<0 or x>=m or y<0 or y>=n or grid2[x][y]==0:
            return True
        if grid1[x][y] == 0:
            return False
        grid2[x][y]=0
        res = True
        for dx,dy in dirs:
            res &= dfs(x+dx,y+dy)
        return res
    
    m, n = len(grid2), len(grid2[0])
    dirs = [(0,1),(1,0),(0,-1),(-1,0)]
    subisls = 0
    for i in range(m):
        for j in range(n):
            if grid2[i][j]==1:
                if dfs(i,j):
                    subisls += 1
    return subisls



