def productQueries(n: int, queries: List[List[int]]) -> List[int]:
    mod = 10**9+7
    bidx = 0
    pwrs = []
    while n:
        if n & 1:
            pwrs.append(1<<bidx)
        n //= 2
        bidx += 1
    
    res = []
    for le,ri in queries:
        prod = 1
        for i in range(le,ri+1):
            prod = (prod*pwrs[i])%mod
        res.append(prod)
    return res

print(productQueries(15, [[0,1],[2,2],[0,3]]))
print(productQueries(2, [[0,0]]))
