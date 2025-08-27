def lenOfVDiagonal(grid: List[List[int]]) -> int:
    dirs = [(1,1),(1,-1),(-1,-1),(-1,1)]
    m,n = len(grid),len(grid[0])

    @cache
    def dfs(cx,cy,dir, turn, targ):
        nx, ny=cx+dirs[dir][0], cy+dirs[dir][1]
        if nx<0 or ny<0 or nx>=m or ny>=n or grid[nx][ny] != targ:
            return 0
        tint = 1 if turn else 0
        maxs = dfs(nx,ny,dir,turn,2-targ)
        if turn:
            maxs = max(maxs, dfs(nx,ny,(dir+1)%4,False,2-targ))
        return maxs+1
    
    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                for dir in range(4):
                    res = max(res, dfs(i,j,dir,True,2)+1)
    return res


print(lenOfVDiagonal())
