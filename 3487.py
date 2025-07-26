def maxSum(self, nums: List[int]) -> int:
        maxi = max(nums)
        if maxi < 0:
            return maxi
        st = set(nums)
        maxs = 0

        for n in st:
            if n > 0:
                maxs += n
        return maxs

print(maxSum([1,2,3,4,5]))  #should be 15
print(maxSum([1,1,0,1,1]))  #should be 1
print(maxSum([-1,-2,1,2,-1,0,1]))  #should be 3
print(maxSum([-100]))  #should be -100
