def findMaxK(nums: list[int]) -> int:
    res = -1
    seen = set()

    for n in nums:
        if -n in seen:
            res = max(res, abs(n))
        else:
            seen.add(n)

    return res


if __name__ == '__main__':
    print(findMaxK([-1, 2, -3, 3]))
    print(findMaxK([-1, 10, 6, 7, -7, 1]))
    print(findMaxK([-10, 8, 6, 7, -2, -3]))
