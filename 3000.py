def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
    maxdisq = 0
    maxarea = 0
    for l,w in dimensions:
        disq = l*l+w*w
        area = l*w
        if disq > maxdisq:
            maxdisq = disq
            maxarea = area
        elif disq == maxdisq:
            maxarea = max(maxarea, area)
    return maxarea

print(areaOfMaxDiagonal([[9,3],[8,6]]))
print(areaOfMaxDiagonal([[3,4],[4,3]]))
