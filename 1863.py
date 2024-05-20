def subsetXORSum(nums: list[int]) -> int:
    res = 0
    for n in nums:
        res |= n
    
    return res << (len(nums)-1)

if __name__ == '__main__':
  print(subsetXORSum([1,3]))
  print(subsetXORSum([5,1,6]))
  print(subsetXORSum([3,4,5,6,7,8]))
