def smallestCommonElement(mat: List[List[int]]) -> int:
    m = len(mat)
    n = len(mat[0])
    di = dict()
    for i in range(m):
        for j in range(n):
            if mat[i][j] not in di.keys():
                di[mat[i][j]] = 1
            else:
                di[mat[i][j]] += 1
    for k,v in di.items():
        if v == m:
            return k
    return -1

print(smallestCommonElement([[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]))
print(smallestCommonElement([[1,2,3],[2,3,4],[2,3,5]]))
