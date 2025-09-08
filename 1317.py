def getNoZeroIntegers(n: int) -> List[int]:
    res = []
    for i in range(n):
        a = i
        b = n-i
        if str(a).count('0')==0 and str(b).count('0')==0:
            res.append(a)
            res.append(b)
            break
    return res


print(getNoZeroIntegers(2))
print(getNoZeroIntegers(11))
