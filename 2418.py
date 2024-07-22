def sortPeople(names: List[str], heights: List[int]) -> List[str]:
    di = dict(zip(heights,names))
    hsort = sorted(heights, reverse=True)
    return [di[h] for h in hsort]



if __name__ == '__main__':
    print(sortPeople(["Mary","John","Emma"],[180,165,170]))
    print(sortPeople(["Alice","Bob","Bob"],[155,185,150]))
