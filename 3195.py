def minimumArea(grid: List[List[int]]) -> int:
    m,n = len(grid), len(grid[0])
    mini, minj = n, m
    maxi, maxj = 0, 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                mini = min(mini, i)
                minj = min(minj, j)
                maxi = max(maxi, i)
                maxj = max(maxj, j)
    return (maxi-mini+1)*(maxj-minj+1)

print(minimumArea([[0,1,0],[1,0,1]]))
print(minimumArea([[1,0],[0,0]]))
