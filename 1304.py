def sumZero(self, n: int) -> List[int]:
    res = []
    if n%2==1:
        res.append(0)
    for i in range(1, n//2+1):
        res.append(i)
        res.append(-i)
    return res

print(sumZero(5))
print(sumZero(3))
print(sumZero(1))
