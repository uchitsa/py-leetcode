def longestNiceSubarray(nums) -> int:
    n = len(nums)
    beg = 0
    maxi = 0
    curma = 0
    for end in range(n):
        while (curma & nums[end]) != 0:
            curma ^= nums[beg]
            beg += 1
        curma |= nums[end]
        maxi = max(maxi, end-beg+1)
    return maxi

nums = [1,3,8,48,10]
print(longestNiceSubarray(nums))
nums = [3,1,5,11,13]
print(longestNiceSubarray(nums))
