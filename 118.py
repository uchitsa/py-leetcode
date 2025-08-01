def generate(numRows: int) -> List[List[int]]:
    if numRows == 0:
        return []
    res = [[1]]
    if numRows == 1:
        return res
    for i in range(1, numRows):
        r = [1]
        for j in range (1,i):
            r.append(res[i-1][j-1] + res[i-1][j])
        r.append(1)
        res.append(r)
    return res

print(generate(5))
print(generate(1))
