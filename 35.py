def searchInsert(nums: list[int], target: int) -> int:
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
    return lo

if __name__ == '__main__':
    print(searchInsert([1,3,5,6],5))
    print(searchInsert([1,3,5,6],2))
    print(searchInsert([1,3,5,6],7))
