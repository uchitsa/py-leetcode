def numOfUnplacedFruits(fruits, baskets) -> int:
    cnt = 0
    for fru in fruits:
        unst = 1
        for i in range(len(baskets)):
            if fru <= baskets[i]:
                baskets[i] = 0
                unst = 0
                break
        cnt += unst
    return cnt

print(numOfUnplacedFruits([4],[4]))
print(numOfUnplacedFruits([3,6,1],[6,4,7]))
print(numOfUnplacedFruits([4,2,5],[3,5,4]))
