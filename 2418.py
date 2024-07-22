def sortPeople(names: List[str], heights: List[int]) -> List[str]:
    di = dict(zip(heights,names))
    hsort = sorted(heights, reverse=True)
    return [di[h] for h in hsort]
