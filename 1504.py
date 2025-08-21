def numSubmat(mat: List[List[int]]) -> int:
    res = 0
    r = [[0]*len(mat[0]) for _ in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if j == 0:
                r[i][j]=mat[i][j]
            else:
                r[i][j] = 0 if mat[i][j] == 0 else r[i][j-1]+1
            c = r[i][j]
            for k in range(i,-1,-1):
                c = min(c,r[k][j])
                if c == 0:
                    break
                res += c
    return res

print(numSubmat([[1,0,1],[1,1,0],[1,1,0]]))
print(numSubmat([[0,1,1,0],[0,1,1,1],[1,1,1,0]]))
