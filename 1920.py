def buildArray(nums: List[int]) -> List[int]:
    ans = [0]*len(nums)
    for i in range(0,len(nums)):
        ans[i] = nums[nums[i]]
    return ans

if __name__ == '__main__':
    print(buildArray([0,2,1,5,3,4]))
    print(buildArray([5,0,1,2,3,4]))
