def countHillValley(nums: List[int]) -> int:
  cnt = 0
  le = nums[0]
  for i in range(1,len(nums)-1):
      if nums[i] != nums[i+1]:
          if le < nums[i] > nums[i+1] or le > nums[i] < nums[i+1]:
              cnt += 1
          le = nums[i]
  return cnt

print(countHillValley([2,4,1,1,6,5]))  #should be 3
print(countHillValley([6,6,5,5,4,1]))  #should be 0
