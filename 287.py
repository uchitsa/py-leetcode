def findDuplicate( nums: list[int]) -> int:
    lo = nums[0]
    hi = nums[0]
    while True:
        lo = nums[lo]
        hi = nums[nums[hi]]
        if lo == hi:
            break
    hi = nums[0]
    while lo != hi:
        lo = nums[lo]
        hi = nums[hi]
    return lo

if __name__ == '__main__':
    print(findDuplicate([1,3,4,2,2]))
    print(findDuplicate([3,1,3,4,2]))
    print(findDuplicate([3,3,3,3,3]))
