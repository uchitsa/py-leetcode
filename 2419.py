def longestSubarray(nums) -> int:
    maxi = max(nums)
    maxlen, curlen = 0, 0
    for n in nums:
        if n == maxi:
            curlen += 1
            maxlen = max(maxlen, curlen)
        else:
            curlen = 0
    return maxlen

print(longestSubarray([1,2,3,4,5]))
print(longestSubarray([1,2,3,3,2,2]))
