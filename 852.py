def peakIndexInMountainArray(arr: list[int]) -> int:
    lo = 0
    hi = len(arr)-1
    while lo<hi:
        mi = (lo + hi)//2
        if arr[mi]>arr[mi+1]:
            hi = mi
        else:
            lo = mi + 1
    return lo


if __name__ == '__main__':
    print(peakIndexInMountainArray([0,1,0]))
    print(peakIndexInMountainArray([0,2,1,0]))
    print(peakIndexInMountainArray([0,10,5,2]))
