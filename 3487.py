def maxSum(nums: List[int]) -> int:
        st = set(nums)
        maxs = sum(st)

        neo = list(st)
        while len(neo)>1:
            neo.remove(min(neo))
            if sum(neo) > maxs:
                maxs = sum(neo)
            else:
                return maxs
        return maxs

print(maxSum([1,2,3,4,5]))  #should be 15
print(maxSum([1,1,0,1,1]))  #should be 1
print(maxSum([-1,-2,1,2,-1,0,1]))  #should be 3
print(maxSum([-100]))  #should be -100
