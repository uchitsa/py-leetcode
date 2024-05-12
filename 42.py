def trap(height: list[int]) -> int:
    le, leMax = 0, 0
    ri = len(height) - 1
    riMax = 0
    vol = 0
    while le <= ri:
        if leMax < riMax:
            if height[le] < leMax:
                vol += leMax - height[le]
            else:
                leMax = height[le]
            le += 1
        else:
            if height[ri] < riMax:
                vol += riMax - height[ri]
            else:
                riMax = height[ri]
            ri -= 1
    return vol


if __name__ == '__main__':
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(trap([4, 2, 0, 3, 2, 5]))
