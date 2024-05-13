def search( nums: list[int], target: int) -> int:
    lo = 0
    hi = len(nums)-1
    mi = (lo + hi)//2
    if nums[mi] == target:
        return mi
    while lo<=hi:
        mi = (lo + hi)//2
        if nums[mi] == target:
            return mi
        if nums[mi] < target:
            lo = mi + 1
        if nums[mi] > target:
            hi = mi - 1
    return -1


if __name__ == '__main__':
    print(search([-1,0,3,5,9,12],9))
    print(search([-1,0,3,5,9,12], 2))
