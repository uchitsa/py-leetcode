import collections
def minCost(basket1: List[int], basket2: List[int]) -> int:
    sum1 = sum(basket1)
    sum2 = sum(basket2)
    if (sum1+sum2)%2 != 0:
        return -1
    trg = (sum1+sum2)//2
    cnt1 = collections.Counter(basket1)
    cnt2 = collections.Counter(basket2)
    totalcnt = cnt1+cnt2
    for n in totalcnt:
        if totalcnt[n]%2!=0:
            return -1
    swap1, swap2 = [], []
    for n in cnt1:
        d = cnt1[n]-(totalcnt[n]//2)
        if d>0:
            swap1.extend([n]*d)
    for n in cnt2:
        d = cnt2[n]-(totalcnt[n]//2)
        if d>0:
            swap2.extend([n]*d)
    swap1.sort()
    swap2.sort()
    minx = min(min(basket1),min(basket2))
    res = 0
    i,j = 0, len(swap2)-1
    while i<len(swap1) and j>=0:
        cst = min(swap1[i],swap2[j])
        res += min(cst, 2*minx)
        i += 1
        j -= 1
    return res

print(minCost([4,2,2,2]))
print(minCost([2,3,4,1]))
