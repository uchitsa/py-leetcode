def longestSubarray(nums: List[int]) -> int:
    zeros = 0
    lngwind = 0
    start = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zeros += 1
        while zeros > 1:
            if nums[start] == 0:
                zeros -= 1 
            start += 1
        lngwind = max(lngwind, i-start)
    return lngwind

print(longestSubarray([1,1,0,1]))
print(longestSubarray([0,1,1,1,0,1,1,0,1]))
print(longestSubarray([1,1,1]))
