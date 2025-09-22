def maxFrequencyElements(nums: List[int]) -> int:
    freq = {}
    for n in nums:
        if n in freq.keys():
            freq[n] += 1
        else:
            freq[n] = 1
    res = 0
    maxi = max(freq.values())
    for v in freq.values():
        if v == maxi:
            res += v
    return res


print(maxFrequencyElements([1,2,2,3,1,4]))
print(maxFrequencyElements([1,2,3,4,5]))
