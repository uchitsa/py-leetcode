def countSquares(matrix: List[List[int]]) -> int:
    r, c = len(matrix), len(matrix[0])
    t =[([0]*(c+1)) for _ in range(r+1)]
    res = 0
    for i in range(r):
        for j in range(c):
            if matrix[i][j]:
                t[i+1][j+1] = (min(t[i][j+1],t[i+1][j],t[i][j])+1)
                res += t[i+1][j+1]
    return res

print(countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))
print(countSquares([[1,0,1],[1,1,0],[1,1,0]]))
