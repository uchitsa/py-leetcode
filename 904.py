def totalFruit(fruits) -> int:
    le = 0
    bsk = {}
    maxi = 0
    for ri, fru in enumerate(fruits):
        bsk[fru] = bsk.get(fru,0)+1
        while len(bsk)>2:
            lefru = fruits[le]
            bsk[lefru] -= 1
            if bsk[lefru] == 0:
                del bsk[lefru]
            le += 1
        maxi = max(maxi, ri-le+1)
    return maxi

print(totalFruit([1,2,1]))
print(totalFruit([0,1,2,2]))
print(totalFruit([1,2,3,2,2]))
