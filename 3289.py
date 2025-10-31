class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        m = {}
        for i in range(len(nums)):
            if nums[i] not in m.keys():
                m[nums[i]] = 1
            else:
                m[nums[i]] += 1
        
        res = []
        for k,v in m.items():
            if v==2:
                res.append(k)
        
        return res
