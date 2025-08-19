def zeroFilledSubarray(nums: List[int]) -> int:
  res = 0
  subs = 0
  for n in nums:
      if n==0:
          subs += 1
      else:
          subs = 0
      res += subs
  return res

print(zeroFilledSubarray([1,3,0,0,2,0,0,4]))
print(zeroFilledSubarray([0,0,0,2,0,0]))
print(zeroFilledSubarray([2,10,2019]))
