def judgePoint24(cards: List[int]) -> bool:
      nums = [*cards]
      return btrk(nums)
  def btrk(nums):
      if len(nums)==1:
          return abs(nums[0]-24)<0.1
      
      for i in range(0,len(nums)):
          for j in range(0,len(nums)):
              if i==j:
                  continue
              next = []
              for k in range(0,len(nums)):
                  if k != i and k != j:
                      next.append(nums[k])
              for op in range(0,4):
                  if op==0:
                      next.append(nums[i]+nums[j])
                  elif op==1:
                      next.append(nums[i]-nums[j])
                  elif op==2:
                      next.append(nums[i]*nums[j])
                  elif op==3 and nums[j]!=0:
                      next.append(nums[i]/nums[j])
                  else:
                      continue
                  if btrk(next):
                      return True
                    next.pop()
        return False

print(judgePoint24([4,1,8,7]))
print(judgePoint24([1,2,1,2]))
