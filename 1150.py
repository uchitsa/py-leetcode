def isMajorityElement(nums: List[int], target: int) -> bool:
    cnt = 0
    for n in nums:
        cnt += 1 if n == target else 0
    return cnt > len(nums)//2

print(isMajorityElement([2,4,5,5,5,5,5,6,6], 5))
print(isMajorityElement([10,100,101,101], 101))
