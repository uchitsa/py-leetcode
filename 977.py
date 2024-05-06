def sortedSquares(nums: list[int]) -> list[int]:
    res = [None] * len(nums)
    le = 0
    ri = len(nums)-1
    i = len(nums)-1
    while i>=0:
        if abs(nums[le]) >= abs(nums[ri]):
            res[i] = nums[le]*nums[le]
            le += 1
        else:
            res[i] = nums[ri]*nums[ri]
            ri -= 1
        i -= 1
    return res


if __name__ == '__main__':
    print(sortedSquares([-4,-1,0,3,10]))
    print(sortedSquares([-7,-3,2,3,11]))
