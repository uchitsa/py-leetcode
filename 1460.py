def canBeEqual(target: list[int], arr: list[int]) -> bool:
    target.sort()
    arr.sort()
    return target == arr


if __name__ == '__main__':
    print(canBeEqual([1, 2, 3, 4], [2, 4, 1, 3]))
    print(canBeEqual([7], [7]))
    print(canBeEqual([3, 7, 9], [3, 7, 11]))
